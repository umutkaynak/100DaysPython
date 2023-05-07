"""#blank state uaztılı img dosyasını turtle kütüphanesinde açarak csv uzantılı dosyanın konumlarına göre denk gelen şehirleri
            haritanın üzerine yazdırma """
import pandas as pd
import turtle
screen=turtle.Screen()
screen.title("US State Oyunu")

#biz de resimdeki gibi görünmesi için
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")#turtle ekranına istenen görüntüyü verebilir
guessed_states = []
#harita üzerine denk gelen koordinatları nasıl bulabiliriz.?
""" 
def mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(mouse_click_coor) #resimde tıklanan yerlerin koordinatlarını ekrana yazırdacak

#bunun yerine csv içinde hazır kodları bulunmakta.
"""




data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 Eyalet Doğru",prompt="eyalet ismini gir")
    print(answer_state)
    if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]# girilen değerin karşılık gelen x ve y değerlerini bul
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
    if answer_state.lower()=="exit": #koddan çıkmak istenirse
          pd.DataFrame(guessed_states).to_csv("bilinenler.csv")
          break




turtle.mainloop()#ekranı açık tutar.
