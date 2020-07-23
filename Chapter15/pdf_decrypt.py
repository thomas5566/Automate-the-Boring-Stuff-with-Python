import os, PyPDF2, sys

password = '5566gb'
decrypt_faild = []

for folders, subfolders, filenames in os.walk('.'):

    for filename in filenames:
        
        if filename.endswith('.pdf'):
            path = os.path.join(folders, filename)
            pdf_obj = open(path, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_obj)

            if pdf_reader.isEncrypted is True:
                if pdf_reader.decrypt(password) != 1:
                    print(filename + ' failed to decrypt.')
                    decrypt_faild.append(filename)

                else:
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))

                        decrypted_path = path[:-4] + '_decrypt.pdf'
                        decrypt_version = open(decrypted_path, 'wb')
                        pdf_writer.write(decrypt_version)
                        decrypt_version.close()

if decrypt_faild != []:
    print('All PDF File is decrypt, except those listed above....')
else:
    print('All PDF files is decrypt Done!!!')


