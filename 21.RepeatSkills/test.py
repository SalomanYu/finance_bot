# from langdetect import detect
# import translators

# a = 'Работа in Adobe After Effects'
# a = "Владение Photoshop, 3D-Coat, Octane Render"
# for i in a.split():
#     try:
#         if detect(i) != 'en':
#             a = a.replace(i, translators.google(i, from_language=detect(i), to_language='en'))
#     except:
#         pass
# print(translators.google(a, from_language='en', to_language='ru'))

for i in range(10): 
    for j in range(i+1, 10):
        print(i, j)
    print('------------')