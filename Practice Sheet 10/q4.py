def greet(fx):
    def mfx():
        print('Hann lode aagya tu?')
        fx()
        print('Hogya kaam Nikal ab\nBye!')
    return mfx    
 
