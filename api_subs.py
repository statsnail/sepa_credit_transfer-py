#!/usr/bin/env python

#
# Generated Sun Jul  9 15:09:01 2017 by generateDS.py version 2.28a.
#
# Command line options:
#   ('-o', 'api.py')
#   ('-s', 'api_subs.py')
#   ('--super', 'api')
#   ('-f', '')
#
# Command line arguments:
#   pain.001.001.03.xsd
#
# Command line:
#   /usr/local/bin/generateDS -o "api.py" -s "api_subs.py" --super="api" -f pain.001.001.03.xsd
#
# Current working directory (os.getcwd()):
#   iso_api
#

import sys
from lxml import etree as etree_

import api as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class AccountIdentification4ChoiceSub(supermod.AccountIdentification4Choice):
    def __init__(self, IBAN=None, Othr=None):
        super(AccountIdentification4ChoiceSub, self).__init__(IBAN, Othr, )
supermod.AccountIdentification4Choice.subclass = AccountIdentification4ChoiceSub
# end class AccountIdentification4ChoiceSub


class AccountSchemeName1ChoiceSub(supermod.AccountSchemeName1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(AccountSchemeName1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.AccountSchemeName1Choice.subclass = AccountSchemeName1ChoiceSub
# end class AccountSchemeName1ChoiceSub


class ActiveOrHistoricCurrencyAndAmountSub(supermod.ActiveOrHistoricCurrencyAndAmount):
    def __init__(self, Ccy=None, valueOf_=None):
        super(ActiveOrHistoricCurrencyAndAmountSub, self).__init__(Ccy, valueOf_, )
supermod.ActiveOrHistoricCurrencyAndAmount.subclass = ActiveOrHistoricCurrencyAndAmountSub
# end class ActiveOrHistoricCurrencyAndAmountSub


class AmountType3ChoiceSub(supermod.AmountType3Choice):
    def __init__(self, InstdAmt=None, EqvtAmt=None):
        super(AmountType3ChoiceSub, self).__init__(InstdAmt, EqvtAmt, )
supermod.AmountType3Choice.subclass = AmountType3ChoiceSub
# end class AmountType3ChoiceSub


class Authorisation1ChoiceSub(supermod.Authorisation1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(Authorisation1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.Authorisation1Choice.subclass = Authorisation1ChoiceSub
# end class Authorisation1ChoiceSub


class BranchAndFinancialInstitutionIdentification4Sub(supermod.BranchAndFinancialInstitutionIdentification4):
    def __init__(self, FinInstnId=None, BrnchId=None):
        super(BranchAndFinancialInstitutionIdentification4Sub, self).__init__(FinInstnId, BrnchId, )
supermod.BranchAndFinancialInstitutionIdentification4.subclass = BranchAndFinancialInstitutionIdentification4Sub
# end class BranchAndFinancialInstitutionIdentification4Sub


class BranchData2Sub(supermod.BranchData2):
    def __init__(self, Id=None, Nm=None, PstlAdr=None):
        super(BranchData2Sub, self).__init__(Id, Nm, PstlAdr, )
supermod.BranchData2.subclass = BranchData2Sub
# end class BranchData2Sub


class CashAccount16Sub(supermod.CashAccount16):
    def __init__(self, Id=None, Tp=None, Ccy=None, Nm=None):
        super(CashAccount16Sub, self).__init__(Id, Tp, Ccy, Nm, )
supermod.CashAccount16.subclass = CashAccount16Sub
# end class CashAccount16Sub


class CashAccountType2Sub(supermod.CashAccountType2):
    def __init__(self, Cd=None, Prtry=None):
        super(CashAccountType2Sub, self).__init__(Cd, Prtry, )
supermod.CashAccountType2.subclass = CashAccountType2Sub
# end class CashAccountType2Sub


class CategoryPurpose1ChoiceSub(supermod.CategoryPurpose1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(CategoryPurpose1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.CategoryPurpose1Choice.subclass = CategoryPurpose1ChoiceSub
# end class CategoryPurpose1ChoiceSub


class Cheque6Sub(supermod.Cheque6):
    def __init__(self, ChqTp=None, ChqNb=None, ChqFr=None, DlvryMtd=None, DlvrTo=None, InstrPrty=None, ChqMtrtyDt=None, FrmsCd=None, MemoFld=None, RgnlClrZone=None, PrtLctn=None):
        super(Cheque6Sub, self).__init__(ChqTp, ChqNb, ChqFr, DlvryMtd, DlvrTo, InstrPrty, ChqMtrtyDt, FrmsCd, MemoFld, RgnlClrZone, PrtLctn, )
supermod.Cheque6.subclass = Cheque6Sub
# end class Cheque6Sub


class ChequeDeliveryMethod1ChoiceSub(supermod.ChequeDeliveryMethod1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ChequeDeliveryMethod1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ChequeDeliveryMethod1Choice.subclass = ChequeDeliveryMethod1ChoiceSub
# end class ChequeDeliveryMethod1ChoiceSub


class ClearingSystemIdentification2ChoiceSub(supermod.ClearingSystemIdentification2Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ClearingSystemIdentification2ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ClearingSystemIdentification2Choice.subclass = ClearingSystemIdentification2ChoiceSub
# end class ClearingSystemIdentification2ChoiceSub


class ClearingSystemMemberIdentification2Sub(supermod.ClearingSystemMemberIdentification2):
    def __init__(self, ClrSysId=None, MmbId=None):
        super(ClearingSystemMemberIdentification2Sub, self).__init__(ClrSysId, MmbId, )
supermod.ClearingSystemMemberIdentification2.subclass = ClearingSystemMemberIdentification2Sub
# end class ClearingSystemMemberIdentification2Sub


class ContactDetails2Sub(supermod.ContactDetails2):
    def __init__(self, NmPrfx=None, Nm=None, PhneNb=None, MobNb=None, FaxNb=None, EmailAdr=None, Othr=None):
        super(ContactDetails2Sub, self).__init__(NmPrfx, Nm, PhneNb, MobNb, FaxNb, EmailAdr, Othr, )
supermod.ContactDetails2.subclass = ContactDetails2Sub
# end class ContactDetails2Sub


class CreditTransferTransactionInformation10Sub(supermod.CreditTransferTransactionInformation10):
    def __init__(self, PmtId=None, PmtTpInf=None, Amt=None, XchgRateInf=None, ChrgBr=None, ChqInstr=None, UltmtDbtr=None, IntrmyAgt1=None, IntrmyAgt1Acct=None, IntrmyAgt2=None, IntrmyAgt2Acct=None, IntrmyAgt3=None, IntrmyAgt3Acct=None, CdtrAgt=None, CdtrAgtAcct=None, Cdtr=None, CdtrAcct=None, UltmtCdtr=None, InstrForCdtrAgt=None, InstrForDbtrAgt=None, Purp=None, RgltryRptg=None, Tax=None, RltdRmtInf=None, RmtInf=None):
        super(CreditTransferTransactionInformation10Sub, self).__init__(PmtId, PmtTpInf, Amt, XchgRateInf, ChrgBr, ChqInstr, UltmtDbtr, IntrmyAgt1, IntrmyAgt1Acct, IntrmyAgt2, IntrmyAgt2Acct, IntrmyAgt3, IntrmyAgt3Acct, CdtrAgt, CdtrAgtAcct, Cdtr, CdtrAcct, UltmtCdtr, InstrForCdtrAgt, InstrForDbtrAgt, Purp, RgltryRptg, Tax, RltdRmtInf, RmtInf, )
supermod.CreditTransferTransactionInformation10.subclass = CreditTransferTransactionInformation10Sub
# end class CreditTransferTransactionInformation10Sub


class CreditorReferenceInformation2Sub(supermod.CreditorReferenceInformation2):
    def __init__(self, Tp=None, Ref=None):
        super(CreditorReferenceInformation2Sub, self).__init__(Tp, Ref, )
supermod.CreditorReferenceInformation2.subclass = CreditorReferenceInformation2Sub
# end class CreditorReferenceInformation2Sub


class CreditorReferenceType1ChoiceSub(supermod.CreditorReferenceType1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(CreditorReferenceType1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.CreditorReferenceType1Choice.subclass = CreditorReferenceType1ChoiceSub
# end class CreditorReferenceType1ChoiceSub


class CreditorReferenceType2Sub(supermod.CreditorReferenceType2):
    def __init__(self, CdOrPrtry=None, Issr=None):
        super(CreditorReferenceType2Sub, self).__init__(CdOrPrtry, Issr, )
supermod.CreditorReferenceType2.subclass = CreditorReferenceType2Sub
# end class CreditorReferenceType2Sub


class CustomerCreditTransferInitiationV03Sub(supermod.CustomerCreditTransferInitiationV03):
    def __init__(self, GrpHdr=None, PmtInf=None):
        super(CustomerCreditTransferInitiationV03Sub, self).__init__(GrpHdr, PmtInf, )
supermod.CustomerCreditTransferInitiationV03.subclass = CustomerCreditTransferInitiationV03Sub
# end class CustomerCreditTransferInitiationV03Sub


class DateAndPlaceOfBirthSub(supermod.DateAndPlaceOfBirth):
    def __init__(self, BirthDt=None, PrvcOfBirth=None, CityOfBirth=None, CtryOfBirth=None):
        super(DateAndPlaceOfBirthSub, self).__init__(BirthDt, PrvcOfBirth, CityOfBirth, CtryOfBirth, )
supermod.DateAndPlaceOfBirth.subclass = DateAndPlaceOfBirthSub
# end class DateAndPlaceOfBirthSub


class DatePeriodDetailsSub(supermod.DatePeriodDetails):
    def __init__(self, FrDt=None, ToDt=None):
        super(DatePeriodDetailsSub, self).__init__(FrDt, ToDt, )
supermod.DatePeriodDetails.subclass = DatePeriodDetailsSub
# end class DatePeriodDetailsSub


class DocumentSub(supermod.Document):
    def __init__(self, CstmrCdtTrfInitn=None):
        super(DocumentSub, self).__init__(CstmrCdtTrfInitn, )
supermod.Document.subclass = DocumentSub
# end class DocumentSub


class DocumentAdjustment1Sub(supermod.DocumentAdjustment1):
    def __init__(self, Amt=None, CdtDbtInd=None, Rsn=None, AddtlInf=None):
        super(DocumentAdjustment1Sub, self).__init__(Amt, CdtDbtInd, Rsn, AddtlInf, )
supermod.DocumentAdjustment1.subclass = DocumentAdjustment1Sub
# end class DocumentAdjustment1Sub


class EquivalentAmount2Sub(supermod.EquivalentAmount2):
    def __init__(self, Amt=None, CcyOfTrf=None):
        super(EquivalentAmount2Sub, self).__init__(Amt, CcyOfTrf, )
supermod.EquivalentAmount2.subclass = EquivalentAmount2Sub
# end class EquivalentAmount2Sub


class ExchangeRateInformation1Sub(supermod.ExchangeRateInformation1):
    def __init__(self, XchgRate=None, RateTp=None, CtrctId=None):
        super(ExchangeRateInformation1Sub, self).__init__(XchgRate, RateTp, CtrctId, )
supermod.ExchangeRateInformation1.subclass = ExchangeRateInformation1Sub
# end class ExchangeRateInformation1Sub


class FinancialIdentificationSchemeName1ChoiceSub(supermod.FinancialIdentificationSchemeName1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(FinancialIdentificationSchemeName1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.FinancialIdentificationSchemeName1Choice.subclass = FinancialIdentificationSchemeName1ChoiceSub
# end class FinancialIdentificationSchemeName1ChoiceSub


class FinancialInstitutionIdentification7Sub(supermod.FinancialInstitutionIdentification7):
    def __init__(self, BIC=None, ClrSysMmbId=None, Nm=None, PstlAdr=None, Othr=None):
        super(FinancialInstitutionIdentification7Sub, self).__init__(BIC, ClrSysMmbId, Nm, PstlAdr, Othr, )
supermod.FinancialInstitutionIdentification7.subclass = FinancialInstitutionIdentification7Sub
# end class FinancialInstitutionIdentification7Sub


class GenericAccountIdentification1Sub(supermod.GenericAccountIdentification1):
    def __init__(self, Id=None, SchmeNm=None, Issr=None):
        super(GenericAccountIdentification1Sub, self).__init__(Id, SchmeNm, Issr, )
supermod.GenericAccountIdentification1.subclass = GenericAccountIdentification1Sub
# end class GenericAccountIdentification1Sub


class GenericFinancialIdentification1Sub(supermod.GenericFinancialIdentification1):
    def __init__(self, Id=None, SchmeNm=None, Issr=None):
        super(GenericFinancialIdentification1Sub, self).__init__(Id, SchmeNm, Issr, )
supermod.GenericFinancialIdentification1.subclass = GenericFinancialIdentification1Sub
# end class GenericFinancialIdentification1Sub


class GenericOrganisationIdentification1Sub(supermod.GenericOrganisationIdentification1):
    def __init__(self, Id=None, SchmeNm=None, Issr=None):
        super(GenericOrganisationIdentification1Sub, self).__init__(Id, SchmeNm, Issr, )
supermod.GenericOrganisationIdentification1.subclass = GenericOrganisationIdentification1Sub
# end class GenericOrganisationIdentification1Sub


class GenericPersonIdentification1Sub(supermod.GenericPersonIdentification1):
    def __init__(self, Id=None, SchmeNm=None, Issr=None):
        super(GenericPersonIdentification1Sub, self).__init__(Id, SchmeNm, Issr, )
supermod.GenericPersonIdentification1.subclass = GenericPersonIdentification1Sub
# end class GenericPersonIdentification1Sub


class GroupHeader32Sub(supermod.GroupHeader32):
    def __init__(self, MsgId=None, CreDtTm=None, Authstn=None, NbOfTxs=None, CtrlSum=None, InitgPty=None, FwdgAgt=None):
        super(GroupHeader32Sub, self).__init__(MsgId, CreDtTm, Authstn, NbOfTxs, CtrlSum, InitgPty, FwdgAgt, )
supermod.GroupHeader32.subclass = GroupHeader32Sub
# end class GroupHeader32Sub


class InstructionForCreditorAgent1Sub(supermod.InstructionForCreditorAgent1):
    def __init__(self, Cd=None, InstrInf=None):
        super(InstructionForCreditorAgent1Sub, self).__init__(Cd, InstrInf, )
supermod.InstructionForCreditorAgent1.subclass = InstructionForCreditorAgent1Sub
# end class InstructionForCreditorAgent1Sub


class LocalInstrument2ChoiceSub(supermod.LocalInstrument2Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(LocalInstrument2ChoiceSub, self).__init__(Cd, Prtry, )
supermod.LocalInstrument2Choice.subclass = LocalInstrument2ChoiceSub
# end class LocalInstrument2ChoiceSub


class NameAndAddress10Sub(supermod.NameAndAddress10):
    def __init__(self, Nm=None, Adr=None):
        super(NameAndAddress10Sub, self).__init__(Nm, Adr, )
supermod.NameAndAddress10.subclass = NameAndAddress10Sub
# end class NameAndAddress10Sub


class OrganisationIdentification4Sub(supermod.OrganisationIdentification4):
    def __init__(self, BICOrBEI=None, Othr=None):
        super(OrganisationIdentification4Sub, self).__init__(BICOrBEI, Othr, )
supermod.OrganisationIdentification4.subclass = OrganisationIdentification4Sub
# end class OrganisationIdentification4Sub


class OrganisationIdentificationSchemeName1ChoiceSub(supermod.OrganisationIdentificationSchemeName1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(OrganisationIdentificationSchemeName1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.OrganisationIdentificationSchemeName1Choice.subclass = OrganisationIdentificationSchemeName1ChoiceSub
# end class OrganisationIdentificationSchemeName1ChoiceSub


class Party6ChoiceSub(supermod.Party6Choice):
    def __init__(self, OrgId=None, PrvtId=None):
        super(Party6ChoiceSub, self).__init__(OrgId, PrvtId, )
supermod.Party6Choice.subclass = Party6ChoiceSub
# end class Party6ChoiceSub


class PartyIdentification32Sub(supermod.PartyIdentification32):
    def __init__(self, Nm=None, PstlAdr=None, Id=None, CtryOfRes=None, CtctDtls=None):
        super(PartyIdentification32Sub, self).__init__(Nm, PstlAdr, Id, CtryOfRes, CtctDtls, )
supermod.PartyIdentification32.subclass = PartyIdentification32Sub
# end class PartyIdentification32Sub


class PaymentIdentification1Sub(supermod.PaymentIdentification1):
    def __init__(self, InstrId=None, EndToEndId=None):
        super(PaymentIdentification1Sub, self).__init__(InstrId, EndToEndId, )
supermod.PaymentIdentification1.subclass = PaymentIdentification1Sub
# end class PaymentIdentification1Sub


class PaymentInstructionInformation3Sub(supermod.PaymentInstructionInformation3):
    def __init__(self, PmtInfId=None, PmtMtd=None, BtchBookg=None, NbOfTxs=None, CtrlSum=None, PmtTpInf=None, ReqdExctnDt=None, PoolgAdjstmntDt=None, Dbtr=None, DbtrAcct=None, DbtrAgt=None, DbtrAgtAcct=None, UltmtDbtr=None, ChrgBr=None, ChrgsAcct=None, ChrgsAcctAgt=None, CdtTrfTxInf=None):
        super(PaymentInstructionInformation3Sub, self).__init__(PmtInfId, PmtMtd, BtchBookg, NbOfTxs, CtrlSum, PmtTpInf, ReqdExctnDt, PoolgAdjstmntDt, Dbtr, DbtrAcct, DbtrAgt, DbtrAgtAcct, UltmtDbtr, ChrgBr, ChrgsAcct, ChrgsAcctAgt, CdtTrfTxInf, )
supermod.PaymentInstructionInformation3.subclass = PaymentInstructionInformation3Sub
# end class PaymentInstructionInformation3Sub


class PaymentTypeInformation19Sub(supermod.PaymentTypeInformation19):
    def __init__(self, InstrPrty=None, SvcLvl=None, LclInstrm=None, CtgyPurp=None):
        super(PaymentTypeInformation19Sub, self).__init__(InstrPrty, SvcLvl, LclInstrm, CtgyPurp, )
supermod.PaymentTypeInformation19.subclass = PaymentTypeInformation19Sub
# end class PaymentTypeInformation19Sub


class PersonIdentification5Sub(supermod.PersonIdentification5):
    def __init__(self, DtAndPlcOfBirth=None, Othr=None):
        super(PersonIdentification5Sub, self).__init__(DtAndPlcOfBirth, Othr, )
supermod.PersonIdentification5.subclass = PersonIdentification5Sub
# end class PersonIdentification5Sub


class PersonIdentificationSchemeName1ChoiceSub(supermod.PersonIdentificationSchemeName1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(PersonIdentificationSchemeName1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.PersonIdentificationSchemeName1Choice.subclass = PersonIdentificationSchemeName1ChoiceSub
# end class PersonIdentificationSchemeName1ChoiceSub


class PostalAddress6Sub(supermod.PostalAddress6):
    def __init__(self, AdrTp=None, Dept=None, SubDept=None, StrtNm=None, BldgNb=None, PstCd=None, TwnNm=None, CtrySubDvsn=None, Ctry=None, AdrLine=None):
        super(PostalAddress6Sub, self).__init__(AdrTp, Dept, SubDept, StrtNm, BldgNb, PstCd, TwnNm, CtrySubDvsn, Ctry, AdrLine, )
supermod.PostalAddress6.subclass = PostalAddress6Sub
# end class PostalAddress6Sub


class Purpose2ChoiceSub(supermod.Purpose2Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(Purpose2ChoiceSub, self).__init__(Cd, Prtry, )
supermod.Purpose2Choice.subclass = Purpose2ChoiceSub
# end class Purpose2ChoiceSub


class ReferredDocumentInformation3Sub(supermod.ReferredDocumentInformation3):
    def __init__(self, Tp=None, Nb=None, RltdDt=None):
        super(ReferredDocumentInformation3Sub, self).__init__(Tp, Nb, RltdDt, )
supermod.ReferredDocumentInformation3.subclass = ReferredDocumentInformation3Sub
# end class ReferredDocumentInformation3Sub


class ReferredDocumentType1ChoiceSub(supermod.ReferredDocumentType1Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ReferredDocumentType1ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ReferredDocumentType1Choice.subclass = ReferredDocumentType1ChoiceSub
# end class ReferredDocumentType1ChoiceSub


class ReferredDocumentType2Sub(supermod.ReferredDocumentType2):
    def __init__(self, CdOrPrtry=None, Issr=None):
        super(ReferredDocumentType2Sub, self).__init__(CdOrPrtry, Issr, )
supermod.ReferredDocumentType2.subclass = ReferredDocumentType2Sub
# end class ReferredDocumentType2Sub


class RegulatoryAuthority2Sub(supermod.RegulatoryAuthority2):
    def __init__(self, Nm=None, Ctry=None):
        super(RegulatoryAuthority2Sub, self).__init__(Nm, Ctry, )
supermod.RegulatoryAuthority2.subclass = RegulatoryAuthority2Sub
# end class RegulatoryAuthority2Sub


class RegulatoryReporting3Sub(supermod.RegulatoryReporting3):
    def __init__(self, DbtCdtRptgInd=None, Authrty=None, Dtls=None):
        super(RegulatoryReporting3Sub, self).__init__(DbtCdtRptgInd, Authrty, Dtls, )
supermod.RegulatoryReporting3.subclass = RegulatoryReporting3Sub
# end class RegulatoryReporting3Sub


class RemittanceAmount1Sub(supermod.RemittanceAmount1):
    def __init__(self, DuePyblAmt=None, DscntApldAmt=None, CdtNoteAmt=None, TaxAmt=None, AdjstmntAmtAndRsn=None, RmtdAmt=None):
        super(RemittanceAmount1Sub, self).__init__(DuePyblAmt, DscntApldAmt, CdtNoteAmt, TaxAmt, AdjstmntAmtAndRsn, RmtdAmt, )
supermod.RemittanceAmount1.subclass = RemittanceAmount1Sub
# end class RemittanceAmount1Sub


class RemittanceInformation5Sub(supermod.RemittanceInformation5):
    def __init__(self, Ustrd=None, Strd=None):
        super(RemittanceInformation5Sub, self).__init__(Ustrd, Strd, )
supermod.RemittanceInformation5.subclass = RemittanceInformation5Sub
# end class RemittanceInformation5Sub


class RemittanceLocation2Sub(supermod.RemittanceLocation2):
    def __init__(self, RmtId=None, RmtLctnMtd=None, RmtLctnElctrncAdr=None, RmtLctnPstlAdr=None):
        super(RemittanceLocation2Sub, self).__init__(RmtId, RmtLctnMtd, RmtLctnElctrncAdr, RmtLctnPstlAdr, )
supermod.RemittanceLocation2.subclass = RemittanceLocation2Sub
# end class RemittanceLocation2Sub


class ServiceLevel8ChoiceSub(supermod.ServiceLevel8Choice):
    def __init__(self, Cd=None, Prtry=None):
        super(ServiceLevel8ChoiceSub, self).__init__(Cd, Prtry, )
supermod.ServiceLevel8Choice.subclass = ServiceLevel8ChoiceSub
# end class ServiceLevel8ChoiceSub


class StructuredRegulatoryReporting3Sub(supermod.StructuredRegulatoryReporting3):
    def __init__(self, Tp=None, Dt=None, Ctry=None, Cd=None, Amt=None, Inf=None):
        super(StructuredRegulatoryReporting3Sub, self).__init__(Tp, Dt, Ctry, Cd, Amt, Inf, )
supermod.StructuredRegulatoryReporting3.subclass = StructuredRegulatoryReporting3Sub
# end class StructuredRegulatoryReporting3Sub


class StructuredRemittanceInformation7Sub(supermod.StructuredRemittanceInformation7):
    def __init__(self, RfrdDocInf=None, RfrdDocAmt=None, CdtrRefInf=None, Invcr=None, Invcee=None, AddtlRmtInf=None):
        super(StructuredRemittanceInformation7Sub, self).__init__(RfrdDocInf, RfrdDocAmt, CdtrRefInf, Invcr, Invcee, AddtlRmtInf, )
supermod.StructuredRemittanceInformation7.subclass = StructuredRemittanceInformation7Sub
# end class StructuredRemittanceInformation7Sub


class TaxAmount1Sub(supermod.TaxAmount1):
    def __init__(self, Rate=None, TaxblBaseAmt=None, TtlAmt=None, Dtls=None):
        super(TaxAmount1Sub, self).__init__(Rate, TaxblBaseAmt, TtlAmt, Dtls, )
supermod.TaxAmount1.subclass = TaxAmount1Sub
# end class TaxAmount1Sub


class TaxAuthorisation1Sub(supermod.TaxAuthorisation1):
    def __init__(self, Titl=None, Nm=None):
        super(TaxAuthorisation1Sub, self).__init__(Titl, Nm, )
supermod.TaxAuthorisation1.subclass = TaxAuthorisation1Sub
# end class TaxAuthorisation1Sub


class TaxInformation3Sub(supermod.TaxInformation3):
    def __init__(self, Cdtr=None, Dbtr=None, AdmstnZn=None, RefNb=None, Mtd=None, TtlTaxblBaseAmt=None, TtlTaxAmt=None, Dt=None, SeqNb=None, Rcrd=None):
        super(TaxInformation3Sub, self).__init__(Cdtr, Dbtr, AdmstnZn, RefNb, Mtd, TtlTaxblBaseAmt, TtlTaxAmt, Dt, SeqNb, Rcrd, )
supermod.TaxInformation3.subclass = TaxInformation3Sub
# end class TaxInformation3Sub


class TaxParty1Sub(supermod.TaxParty1):
    def __init__(self, TaxId=None, RegnId=None, TaxTp=None):
        super(TaxParty1Sub, self).__init__(TaxId, RegnId, TaxTp, )
supermod.TaxParty1.subclass = TaxParty1Sub
# end class TaxParty1Sub


class TaxParty2Sub(supermod.TaxParty2):
    def __init__(self, TaxId=None, RegnId=None, TaxTp=None, Authstn=None):
        super(TaxParty2Sub, self).__init__(TaxId, RegnId, TaxTp, Authstn, )
supermod.TaxParty2.subclass = TaxParty2Sub
# end class TaxParty2Sub


class TaxPeriod1Sub(supermod.TaxPeriod1):
    def __init__(self, Yr=None, Tp=None, FrToDt=None):
        super(TaxPeriod1Sub, self).__init__(Yr, Tp, FrToDt, )
supermod.TaxPeriod1.subclass = TaxPeriod1Sub
# end class TaxPeriod1Sub


class TaxRecord1Sub(supermod.TaxRecord1):
    def __init__(self, Tp=None, Ctgy=None, CtgyDtls=None, DbtrSts=None, CertId=None, FrmsCd=None, Prd=None, TaxAmt=None, AddtlInf=None):
        super(TaxRecord1Sub, self).__init__(Tp, Ctgy, CtgyDtls, DbtrSts, CertId, FrmsCd, Prd, TaxAmt, AddtlInf, )
supermod.TaxRecord1.subclass = TaxRecord1Sub
# end class TaxRecord1Sub


class TaxRecordDetails1Sub(supermod.TaxRecordDetails1):
    def __init__(self, Prd=None, Amt=None):
        super(TaxRecordDetails1Sub, self).__init__(Prd, Amt, )
supermod.TaxRecordDetails1.subclass = TaxRecordDetails1Sub
# end class TaxRecordDetails1Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from api import *\n\n')
        sys.stdout.write('import api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
