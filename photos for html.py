import os

def save_image_filenames_as_html_list(directory, output_file):
    # Λίστα για να αποθηκεύσουμε τα HTML στοιχεία
    image_tags = []

    # Διάσχιση του φακέλου
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Έλεγχος αν το αρχείο έχει κατάληξη 
            if file.endswith(".JPG") or file.endswith(".PNG") or file.endswith(".jpg") or file.endswith(".png"):
                # Προσθήκη του HTML στοιχείου στη λίστα
                image_tags.append('<li><img src="\\192.168.2.70\mi\photos-videos{}"></li>'.format(file))

    # Αποθήκευση των HTML στοιχείων σε αρχείο .txt
    with open(output_file, 'a') as f:
        for tag in image_tags:
            f.write("{}\n".format(tag))

# Παράδειγμα χρήσης
directory = r'C:\Users\giats\Desktop\my photos website'  # Αντικαταστήστε με τον φάκελο που θέλετε να ελέγξετε
output_file = 'image_list.txt'  # Το όνομα του αρχείου εξόδου

save_image_filenames_as_html_list(directory, output_file)
