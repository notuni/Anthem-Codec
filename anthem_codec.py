import os
try: 
    import dearpygui.dearpygui as dpg
    pass
except ModuleNotFoundError:
    os.system('pip install dearpygui')
    import dearpygui.dearpygui as dpg
    pass
try:
    import random
    pass
except ModuleNotFoundError:
    os.system('pip install random')
    import random
    pass
def encode(text, n):
    encoded_text = ""
    for char in text:
        encoded_char = ord(char) + n # shift each character by 3 positions
        if encoded_char > 127: # wrap around if the shifted value is outside the ASCII range
            encoded_char -= 94
        encoded_text += chr(encoded_char)
    return encoded_text
def decode(encoded_text, key1):
    decoded_text = ""
    for char in encoded_text:
        decoded_char = ord(char) - int(key1) # shift each character back by 3 positions
        if decoded_char < 33: # wrap around if the shifted value is outside the ASCII range
            decoded_char += 94
        decoded_text += chr(decoded_char)
    return decoded_text
dpg.create_context()
with dpg.window(label='Anthem Codec', no_collapse=True, no_resize=True, no_close=True, tag='anthem', show=True):
    dpg.set_primary_window('anthem', True)
    dpg.add_text('Encode: ')
    enc = dpg.add_input_text(label="")
    def ths():
        pin = random.randint(10, 99)
        encoded_v = encode(dpg.get_value(enc), pin)
        encodedd = (f'Encoded Value: {encoded_v} Password: {pin}')
        dpg.add_input_text(default_value=encodedd, readonly=True, parent='anthem')
    dpg.add_button(label='Encode', callback=lambda:ths())
    dpg.add_text('Decode: ')
    decodee = dpg.add_input_text(label="Decode")
    decode_pass = dpg.add_input_text(label='Decode Pin')
    def thss():
        encoded_v = decode(dpg.get_value(decodee), dpg.get_value(decode_pass))
        enc1 = encoded_v.replace('~', ' ')
        encodedd = (f'Decoded Value: {enc1}')
        dpg.add_input_text(default_value=encodedd, readonly=True, parent='anthem')
    dpg.add_button(label='Decode', callback=lambda:thss())
dpg.create_viewport(title='Anthem Codec', width=835, height=697)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
