# input = [
#     "ia bernama tirtha, ...",
#     "ia bernama panji, ...",
#     "ia bernama subroto, ...",
#     "ia bernama gatot, ...",
#     "ia bernama jarot, ...",
# ]
# output = ''
# for teks in input:
#     output += ' '.join(teks.split(",")[0].split(' bernama ')) + '\n'
# print(output)

# source = '<script nonce="upY5Q63JHhbk85WSvSPU6w">'
# hasil = source.split('"')[1]
# print(hasil)


# source = """
# .yt-spec-icon-shape {
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     width: 100%;
#     height: 100%
# }

# .yt-core-attributed-string--inline-flex-mod {
#     display: inline-flex;
#     height: 1.4em
# }

# .yt-core-attributed-string--inline-block-mod {
#     display: inline-block
# }

# .yt-core-attributed-string__image-element--image-alignment-bottom {
#     vertical-align: bottom
# }

# .yt-core-attributed-string__image-element--image-alignment-baseline {
#     vertical-align: baseline
# }

# .yt-core-attributed-string__image-element--image-alignment-vertical-center {
#     align-self: center
# }

# .yt-core-attributed-string__link {
#     text-decoration: none
# }

# .yt-core-attributed-string__link--display-type {
#     display: inline
# }

# .yt-core-attributed-string__link--call-to-action-color {
#     color: #065fd4
# }

# .yt-core-attributed-string__link--overlay-call-to-action-color {
#     color: #3ea6ff
# }

# .yt-core-attributed-string--link-inherit-color .yt-core-attributed-string__link--call-to-action-color {
#     color: inherit
# }
# """
# output = []

# split1 = source.split('.')
# for splited in split1:
#     res = splited.split(' {')[0]
#     if not '\n' in res:
#         output.append('.' + res)
# print(output)

# source = ['All', 'Music', 'Live', 'Gaming', 'Podcast', 'Funny', 'Race']
# gabung = ' - '.join(source)
# print(list(map(lambda item: item.replace('  ', '--'), gabung.replace('-', ' * ').split('*'))))

