print("Добро пожаловать в новеллу игру \"Попробуй выжить в деревне!!!!\". \n Нажмите \"K\" для начала игры")
start = input()
start = "K" 
names = ["Дедушка Саша"]
print("Правила:\n 1.Выполнять и прислушиваться к советам твоего деда.\n 2.Не открывать ночью НИКОМУ дверь.\n 3.Связи в деревне нет, можешь не надеятся на помощь.\n 4.Будь внимателен(льна)!!!.")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("Наступили летние каникулы. Тебе нужно поехать в деревню на несколько дней, так как у твоего дедушки, который жил в деревне стало плохо со здоровьем, ему нужно было уехать, а тебе присматривать за его домом.")
print(F"Перед твоим отьездом из города,{names[0]} тебе сказал: \"Не открывать никому ночью дверь, кто бы это не был, все окна закрыть и зашторить на ночь\"")
print("Тебе это показалось странным, дед был в возрасте, но до этого дед себя так не вел.")
print("Вы приехали в деревню, и все странно на вас смотрели, но ранее такого не было, ведь вы уже приезжали в эту деревню!")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print(f"вы встретили лучшего друга деда, и он спросил у вас: \"А Сашка как поживает? Знаю, что у него было плохо со здоровьем перед отьездом\" \nЧто вы ответите ему?: \n 1.{names[0]} поехал в больницу, должен вернутся через пару дней \n 2.Да не знаю я!!!!! вас это интересовать не должно!!! пока")
active = int(input())
while active!=3:
    if active == 2:
        print("Грубить лучшему другу деда была не самая лучшая идея, вам прописали чапалах и вы проиграли!")
        raise SystemExit
    elif active == 1:
         print("Дед улыбнулся и ничего не заподозрил")
         active = int(input())
         print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
         print("Друг деда насторожно спросил: \"Ты тут один собираешься ночевать?\" \nЧто вы ответите другу деда?: \n1.Да, буду один \n2.Нет. (Наврать и не доверять другу деда.)")
         active= int(input())
         while active!=3:
            if active == 2:
                print("вас расчленили и выбросили в мусорку в первую же ночь, так как вы не узнали важную информацию от друга деда")
                raise SystemExit
            elif active == 1:
                print("Отлично, в дальнейшем вы узнаете важную информацию от друга деда")
                active = int(input())
                print("Друга деда вам рассказал что происходит тут ночью и сказал: \n1.не разговаривать ночью Ни с кем \n2.нельзя ночью выходить на улицу \n3.закрыть и зашторить все окна в доме!!!!")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("Вы пришли домой и легли на кровать. Вы почти уснули и проснулись и услышали громкие стуки в дверь.\n Что вы будете делать? \n1.Подойти к двери и спросить \"Кто там?\"\n2.Не обращать внимание")
                active = int(input())
                while active!=3:
                    if active == 1:
                        print("Вас убили, потому что вы не послушали своего деда и друга деда!!!")
                        raise SystemExit
                    elif active == 2:
                        print("Вы сделали правильное решение")
                        active = int(input())
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                        print("Вы плохо поспали, пытаясь не обращать внимание на стуки в дверь. Но внезапно вы слышите стуки в дверь и говорите чтобы человек уходил немедленно, но с той стороны двери отвечает девушка и говорит что у нее сломалась машина и просит помощи! \n Помочь девушке? \n1.Да\n2.Нет")
                        active = int(input())
                        while active!=3:
                            if active == 1:
                                print("Эта девушка оказалась людоедом и она вас съела, вы проиграли было сказано не открывть дверь НИКОМУ")
                                raise SystemExit
                            elif active == 2:
                                print("Правильно решение друг мой")
                                active = int(input())
                                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                                print("Девушка начала сильно напрашиватся и стучать в дверь, давить на жалость, \n что вы будете делать? \n1.Постараться помочь ей, не выходя из дома, тем самым, общаться через открытое окно \n2.Никак не реагировать и пойти спать к себе в комнату")
                                active = int(input())
                                while active!=3:
                                    if active == 1:
                                        print("GAME OVER - читай правила дундук")
                                        raise SystemExit
                                    elif active == 2:
                                        print("ого, правильно, ты живой, ураураура")
                                        active = int(input())
                                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                                        print("Придя к себе в комнату, через окно увидели, что в открытое окно вашего соседа залезла какая-то тварь, вы хотели позвонить в полицую, но в деревне нет связи \n резко к вам кто то начал стучаться, за дверью вы услышали что это друг вашего деда \n Открыть дверь? \n1.Да \n2.Нет")
                                        active = int(input())
                                        while active!=3:
                                            if active == 1:
                                                print("Вас убили, потому что вы только что видели, что к вашему соседу залезла какая-то тварь")
                                                raise SystemExit
                                            elif active == 2:
                                                print("Ашалеть ты еще жив? Молодец")
                                                active = int(input())
                                                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                                                print("Вы ушли в свою комнату и посмотрели в окно, и увидели что на улице гуляет девушка совсем одна,вы в недоумении ведь вам сказали нельзя гулять ночью, чтобы остаться в живых\n Вдруг вы увидели что ваш сосед превратился в огромную тварь и побежал к девушке, начал разрывать и есть ее, на крики девушки побежали остальные жители\n и тоже начали превращаться в этих монстров")
                                                print("Вдруг одна из тварей обернулась в вашу сторону, другие также начали оборачиваться\n Что вы будете делать?\n1.зашторите окно и побежите в спальню\n2.зашторите окно и побежите на улицу убегать от этих тварей")
                                                active = int(input())
                                                while active!=3:
                                                    if active == 2:
                                                        print("Вы выбежали на улицу и они побежали за вами сделали из вас вкусный шашлык")
                                                        raise SystemExit
                                                    elif active == 1:
                                                        print("Молодец, вас не превратили в шашлык")
                                                        active = int(input())
                                                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                                                        print("Вы лежали на кровати и слышите как монстры идут в сторону вашего дома, но они не смогли попасть к вам в дом, что странно ведь дома был хилым")
                                                        print("Наступило утро, вы выглянули в окно, и посмотрели на место где все происходило, но никаких следов там не осталось\n Вы аккуратно вышли из дома, осмотрели дом, все было в порядке, посмотрев внимательней, вы увидели царапины на доме\n Вдруг к вам со спины подходит и спрашивает: \"Ну как прошла твоя ночь?\" вы были в полном шоке ведь ночью он превратился в тварь и кушал человека \n Что вы будете делать? \n1.Пытаться продолжить диалог\n2.Убежать от соседа в лес")
                                                        active = int(input())
                                                        while active!=3:
                                                            if active == 2:
                                                                print("вы убежали в лес и на вас напал вини пух и сьел вас")
                                                                raise SystemExit
                                                            elif active == 1:
                                                                print("У нас все окей среди своих друзей")
                                                                active = int(input())
                                                                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                                                                print("вы ушли к себе домой и начало темнеть\nЧто вы будете делать?\n1.Зашторить и закрыть окна и двери\n2.Помогать по дому и сделать это чуть позже")
                                                                active = int(input())
                                                                while active!=3:
                                                                    if active == 2:
                                                                        print("Вы не успели и вас убили")
                                                                        raise SystemExit
                                                                    elif active == 1:
                                                                        print("Правильное решение")
                                                                        active = int(input())
                                                                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                                                                        print("Вы уже легли и услышали голос своего соседа:\"ничего не заметил? оберег у нас!!!\" теперь они начали ломиться к вам и разбили окно\n Что будете делать? \n1.Спрятаться в кладовку \n2.Побежать на улицу через чёрный выход \n3.Сражаться с тварями")
                                                                        active = int(input())
                                                                        while active!=3:
                                                                            if active == 1:
                                                                                print("Твари нашли вас и съели тебя")
                                                                                raise SystemExit
                                                                            elif active == 3:
                                                                                print("Тварей было больше и они съели тебя")
                                                                                raise SystemExit
                                                                            elif active == 2:
                                                                                print("Самое правильное решение")
                                                                                active = int(input())
                                                                                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                                                                                print("Вы бежали очень долго и увидели ЖД станцию и сели в электричку и доехали до своего дома\n МОЛОДЕЦ ТЫ ПРОШЕЛ ИГРУ!!!!!")
                                                                                active = int(input)
                                                                


            