#!/usr/bin/env python3

import sys, inspect
import api as api
from datetime import datetime, timedelta, date
import time
from pytz import timezone
import random

def make_CdtTrfTxInf():
    _CdtTrfTxInf = api.CreditTransferTransactionInformation10()
    the_random_identifier = get_random_identifier("snail")
    _CdtTrfTxInf.set_PmtId(api.PaymentIdentification1(InstrId=the_random_identifier,EndToEndId=the_random_identifier))
    _CdtTrfTxInf.set_PmtTpInf(api.PaymentTypeInformation19(InstrPrty="NORM"))
    _CdtTrfTxInf.set_Amt(api.AmountType3Choice(InstdAmt=api.ActiveOrHistoricCurrencyAndAmount(Ccy="NOK", valueOf_="20")))
    _CdtTrfTxInf.set_Cdtr(api.PartyIdentification32(Nm="Joakim Xxx", PstlAdr=api.PostalAddress6(StrtNm="Epleveien Xx", PstCd="4635", TwnNm="Kristiansand", Ctry="NO")))
    _CdtTrfTxInf.set_CdtrAcct(api.CashAccount16(Id=api.AccountIdentification4Choice(Othr=api.GenericAccountIdentification1(Id="00001122222", SchmeNm=api.PersonIdentificationSchemeName1Choice(Cd="BBAN")))))
    _RmtInf = api.RemittanceInformation5()
    _RmtInf.add_Ustrd("Unstructured Remittance Test Message Max 140")
    _CdtTrfTxInf.set_RmtInf(_RmtInf)
    return _CdtTrfTxInf

def make_PmtInf():
    _PmtInf = api.PaymentInstructionInformation3(ReqdExctnDt=date.today().isoformat())
    _PmtInf.set_PmtInfId(get_random_identifier("pmt_snail")) #Max35Text
    _PmtInf.set_PmtMtd("TRF") #PaymentMethod3Code
    _PmtInf.set_NbOfTxs("1") #Max15NumericText
    _PmtInf.set_CtrlSum(20) #DecimalNumber
    _PmtInf.set_PmtTpInf(api.PaymentTypeInformation19(InstrPrty="NORM"))
    #pdb.set_trace()
    #PmtInf.set_ReqdExctnDt("1996-10-11") # Here be dragons
    #print(PmtInf.get_ReqdExctnDt())
    _PmtInf.set_Dbtr(api.PartyIdentification32(Nm="Statsnail AS", PstlAdr=api.PostalAddress6(Ctry="NO")))
    _PmtInf.set_DbtrAcct(api.CashAccount16(Id=api.AccountIdentification4Choice(Othr=api.GenericAccountIdentification1(Id="00001111000", SchmeNm=api.PersonIdentificationSchemeName1Choice(Cd="BANK"))), Ccy="NOK"))
    _PmtInf.set_DbtrAgt(api.BranchAndFinancialInstitutionIdentification4(FinInstnId=api.FinancialInstitutionIdentification7(BIC="SPTRNO22XXX")))
    
    _PmtInf.add_CdtTrfTxInf(make_CdtTrfTxInf()) #CreditTransferTransactionInformation10
    
    return _PmtInf

def get_random_identifier(addit):
    """Returns a random identifier"""     
    utcdate = time.strftime('%Y%m%d', time.gmtime(time.time()))
    randint = random.randrange(1000)
    return '%s.%s.%s' % (addit, utcdate, randint)

def app():
    print("Using the api...")
    print("Today: ", date.today().isoformat())

    doc = api.Document()
    ccti = api.CustomerCreditTransferInitiationV03()

    msgid = get_random_identifier("msg_snail")
    grphdr = api.GroupHeader32(MsgId=msgid,CreDtTm=datetime.utcnow().replace(microsecond=0).isoformat(), NbOfTxs="1")
    the_id_orgid_othr = api.GenericOrganisationIdentification1(Id="915109012")
    the_id_orgid_othr.set_SchmeNm(api.OrganisationIdentificationSchemeName1Choice(Cd="CUST"))
    the_id_orgid = api.OrganisationIdentification4()
    the_id_orgid.add_Othr(the_id_orgid_othr)
    the_id = api.Party6Choice(OrgId=the_id_orgid)
    initgpty = api.PartyIdentification32(Nm="Statsnail AS", Id=the_id)
    grphdr.set_InitgPty(initgpty)
    
    ccti.set_GrpHdr(grphdr)
    
    ccti.add_PmtInf(make_PmtInf()) # Add one payment
    
    doc.set_CstmrCdtTrfInitn(ccti)

    filetest = open("output.xml",'w')
    doc.export(outfile=filetest, level=0)
    filetest.close()
    
if __name__ == '__main__':
    app()
