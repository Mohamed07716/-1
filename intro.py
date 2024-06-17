from pywebio import start_server
from pywebio.input import*
from pywebio.output import *
put_image(open("C:\\OIP.jfif ",'rb',).read())
def sub():
   
    put_html('<p><h3>مرحبا بكم في موقنا لحفظ والاستماع الي القران الكريم</h3></p>').style('color:blue;font-size:13px,')
    input_group(
        'تسجيل الدخول',
        [
            input('Enter your name',name= 'User', type= TEXT ,placeholder="Your Name ..."),
            input('Enter your email ',name='Email',type=TEXT,placeholder='Your Email ...'),
            input('Enter your password',name='Pass',type=PASSWORD,placeholder='Your Password ...')
        ],
    )

start_server(sub , port=9976 , debug= True)