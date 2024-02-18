import os
import csv
import vobject

def read_vcards(folder_path):
    vcards = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.vcf'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                vcards.extend(vobject.readComponents(file.read()))
    return vcards

def extract_info(vcard):
    info = {'name': 'N/A', 'email': 'N/A', 'tel': 'N/A'}
    
    if vcard.fn:
        info['name'] = vcard.fn.value

    emails = [e.value for e in vcard.contents.get('email', [])]
    if emails:
        info['email'] = emails[0]

    tels = [t.value for t in vcard.contents.get('tel', [])]
    if tels:
        info['tel'] = tels[0]

    return info

def vcards_to_csv(vcards, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'email', 'tel']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for vcard in vcards:
            writer.writerow(extract_info(vcard))

def main():
    folder_path = r'C:\Users\gabri\Downloads\WhatsApp Chat - Grupo de Leads (1)'  # Substitua pelo seu diretório
    vcards = read_vcards(folder_path)
    vcards_to_csv(vcards, 'contatos.csv')

if __name__ == "__main__":
    main()
