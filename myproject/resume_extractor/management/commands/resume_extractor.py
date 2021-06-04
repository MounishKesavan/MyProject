from resume_extractor.models import Resume
from django.core.management.base import BaseCommand
import docx2txt
import re
from django.conf import settings
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        directory =  settings.STATIC_DIR +'/resumes/'
        print(directory)
        files = ['Abiral_Pandey_Fullstack_Java.docx','Achyuth Resume_8.docx']
        for file in files:
            result = docx2txt.process(directory+file)
            result = result.split('\n')
            file_name = file.split('.docx')
            file_name = file_name[0].split('/')[-1]
            email = None
            phone_number = None
            f = []
            for i in result:
                if i :
                    f.append(i.strip())
                    email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", i.strip())
                    phone_number_list = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",i.strip())
                    if email_list:
                        email = email_list[0]
                    if phone_number_list:
                        phone_number = phone_number_list[0]
            Resume.objects.create(name=file_name,email=email,phone_number=phone_number)    
        
        self.stdout.write(self.style.SUCCESS('Run successfully'))
