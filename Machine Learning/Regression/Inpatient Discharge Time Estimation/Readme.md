# Analysis of Hospital Inpatient Discharges (SPARCS De-Identified): 2015

The Statewide Planning and Research Cooperative System (SPARCS) Inpatient De-identified File contains discharge level detail on patient characteristics, diagnoses, treatments, services, and charges. This data file contains basic record level detail for the discharge. The de-identified data file does not contain data that is protected health information (PHI) under HIPAA. The health information is not individually identifiable; all data elements considered identifiable have been redacted. For example, the direct identifiers regarding a date have the day and month portion of the date removed.

https://www.kaggle.com/jonasalmeida/2015-deidentified-ny-inpatient-discharge-sparcs

Discharges that are identified as abortion will have some information redacted; PFI, Facility Name, Health Service Area, Hospital County, Operating Certificate, and all provider license numbers. Patient zip code is limited to the first three digits. However, in cases where the population size for the zip code is less than 20,000, if the cell size on patient classification strata are less than 10, or if the record is an abortion then the zip code is blank. The code “OOS” indicates Out of State zip codes. Patient age is presented in age groups: 0 to 17, 18 to 29, 30 to 49, 50 to 69, and 70 or Older. For years beginning with 2011, the variable indicating the type of insurance expected to pay the discharge has changed. Originally it was the Source of Payment. Effective December 2015, it is now the Payment Typology.

There are **2346760 rows** and **37 columns** in the dataset.

The columns in the dataset are: 'Health Service Area', 'Hospital County', 'Operating Certificate Number', 'Facility Id', 'Facility Name', 'Age Group', 'Zip Code - 3 digits', 'Gender', 'Race', 'Ethnicity', 'Length of Stay', 'Type of Admission', 'Patient Disposition', 'Discharge Year', 'CCS Diagnosis Code', 'CCS Diagnosis Description', 'CCS Procedure Code', 'CCS Procedure Description', 'APR DRG Code', 'APR DRG Description', 'APR MDC Code', 'APR MDC Description', 'APR Severity of Illness Code', 'APR Severity of Illness Description', 'APR Risk of Mortality', 'APR Medical Surgical Description', 'Payment Typology 1', 'Payment Typology 2', 'Payment Typology 3', 'Attending Provider License Number', 'Operating Provider License Number', 'Other Provider License Number', 'Birth Weight', 'Abortion Edit Indicator', 'Emergency Department Indicator', 'Total Charges', 'Total Costs'

The target is to predict the length of stay in the hospital.


Due to the size of the dataset, please follow the link to download the csv file.
