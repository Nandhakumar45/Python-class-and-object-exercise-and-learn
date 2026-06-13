import pydicom

# Load the DICOM file
dicom_file = pydicom.dcmread(r"C:\Users\320287287\OneDrive - Philips\Desktop\DICOM Viewer\CF-5053_Feedback Attachment_DICOM and Examcard\DICOM and Examcard\DICOM\New folder\IM_0001")

# Access some metadata
print("Patient Name:", dicom_file.PatientName)
print("Study Date:", dicom_file.StudyDate)
print("Modality:", dicom_file.Modality)