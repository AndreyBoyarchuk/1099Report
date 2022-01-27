from filestack import Client


client=Client('AoZRHtiSATGSGZnvjiuJPz')

new_filelink=client.upload(filepath='bill.pdf')

print(new_filelink.url)