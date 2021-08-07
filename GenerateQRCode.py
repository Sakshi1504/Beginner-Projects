import pyqrcode

#s="https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

s="https://www.linkedin.com/in/sakshi-agrawal97154019/"

url=pyqrcode.create(s)


url.svg("myqrcode.svg", scale=8)