from anticaptchaofficial.imagecaptcha import *

def solve_captcha(path):
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("f54b0c518750b782039c7a81f4f9d400")

   
    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution("captcha.png")
    if captcha_text != 0:
        return captcha_text
    else:
        print("task finished with error "+solver.error_code)
        return -1
    
