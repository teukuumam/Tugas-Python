magic_numbers  = {'jpg' : bytes ([0xFF, 0xD8])}
max_read_size = max(len(m) for m in magic_numbers.values()) # get max size of magic numbers of the dict

with open('21-41-1-SM.pdf', 'rb') as fd:
    file_head = fd.read(max_read_size)

if file_head.startswith(magic_numbers['jpg']):
    print("File Ini benar")

else:
    print("Maaf File salah, silahkan cek kembali File anda")
