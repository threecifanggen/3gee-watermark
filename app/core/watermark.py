from blind_watermark import WaterMark

def encriptor_str(input_file, str_watermark, output_file, password_img=1, password_wm=1):
    bwm1 = WaterMark(password_img=password_img, password_wm=password_wm)
    bwm1.read_img(input_file)
    wm = str_watermark
    bwm1.read_wm(wm, mode='str')
    bwm1.embed(output_file)
    return bwm1

def decipher_str(input_file, str_watermark, password_img=1, password_wm=1):
    len_wm = len(bin(int(str_watermark.encode('utf-8').hex(), base=16))[2:])
    bwm1 = WaterMark(password_img=password_img, password_wm=password_wm)
    wm_extract = bwm1.extract(input_file, wm_shape=len_wm, mode='str')
    return (wm_extract, wm_extract==str_watermark)