import os

def save_image_filenames_as_html_list(directory, output_file):
    # Λίστα για να αποθηκεύσουμε τα HTML στοιχεία
    image_tags = []

    # Διάσχιση του φακέλου
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Έλεγχος αν το αρχείο έχει κατάληξη 
            if file.endswith(".MP4") or file.endswith(".MOV")or file.endswith(".AVI")or file.endswith(".MKV") or file.endswith(".HEVC") or file.endswith(".VP9") or file.endswith(".AV1") or file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".avi") or file.endswith(".mkv") or file.endswith(".hevc") or file.endswith(".vp9") or file.endswith(".av1"):
                # Προσθήκη του HTML στοιχείου στη λίστα
                image_tags.append('<source src="\\192.168.2.70\mi\photos-videos\{}" type="video/mp4">'.format(file))

    # Αποθήκευση των HTML στοιχείων σε αρχείο .txt
    with open(output_file, 'a') as f:
        for tag in image_tags:
            f.write("{}\n".format(tag))

# Παράδειγμα χρήσης
directory = r'C:\Users\giats\Desktop\my photos website'  # Αντικαταστήστε με τον φάκελο που θέλετε να ελέγξετε
output_file = 'image_list.txt'  # Το όνομα του αρχείου εξόδου

save_image_filenames_as_html_list(directory, output_file)
