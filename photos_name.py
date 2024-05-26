import os

def save_image_filenames(directory, output_file):
    # Λίστα για να αποθηκεύσουμε τα ονόματα των αρχείων
    image_filenames = []

    # Διάσχιση του φακέλου
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Έλεγχος αν το αρχείο έχει κατάληξη .jpg ή .png
            if file.endswith(".JPG") or file.endswith(".PNG"):
                image_filenames.append(file)

    # Αποθήκευση των ονομάτων σε αρχείο .txt
    with open(output_file, 'w') as f:
        for filename in image_filenames:
            f.write("{}\n".format(filename))

# Παράδειγμα χρήσης
directory = r' directory '  # Αντικαταστήστε με τον φάκελο που θέλετε να ελέγξετε
output_file = 'image_filenames.txt'  # Το όνομα του αρχείου εξόδου

save_image_filenames(directory, output_file)
