from VNEPy.VNEPy.words import *
from VNEPy.VNEPy.character import Character
from VNEPy.VNE2D.interactions import ExampleButton

# Создание персонажей
ui = Character("Юии", (251, 236, 93))
tito = Character("Тито", (11, 218, 81))
avvtor = Character('', (255, 255, 255))

# Подземелья
fragment = Fragment('1')

fragment.add(Fon('./images/background/подземелье.jpg'))

fragment.add(Phrase("Темень какая... Темень", tito))
fragment.add(Phrase('Мрак', ui))
fragment.add(Phrase("Сумрак, заткнись", tito))
fragment.add(Phrase('Прости', ui))
fragment.add(Phrase('Не бери в голову...', tito))
fragment.add(Phrase('Может фонарь включим?', ui))

fragment.add(Choice(ExampleButton, ('Нет!', '1.1.0'), ('Дававай, только не долго...', '1.1.2')))
fragment.add(Phrase('', avvtor))

fragment_1 = Fragment('1.1.0')
fragment_2 = Fragment('1.1.2')

fragment_2.add(Phrase('A Дававай, только не долго...', tito))
fragment_2.add(Phrase('Смотри кажется там что-то есть!', ui))
fragment_2.add(Phrase('Да, и в правду', tito))
fragment_2.add(Phrase('Давай проверим, может найдем что-то ценное...', ui))
fragment_2.add(Phrase('Я дуиаю это плохая идея', tito))
fragment_2.add(Phrase('Нуууууу', ui))
fragment_2.add(Phrase('Хорошо давай проверим.', tito))
fragment_2.add(Phrase('Урааааааа!', ui))

fragment_2.add(Phrase('Спустя неокторое время...', avvtor))

fragment_2.add(Phrase('Что? Где это мы?', tito))
fragment_2.add(Phrase('Кажется мы в какойто комнате или что-то в роде этого.', ui))
fragment_2.add(Phrase('Это я и сама поняла... Давай выбераться отсюда', tito))
fragment_2.add(Phrase('Хорошая идея!', ui))
fragment_2.add(Phrase('Смотри! Кажется там что-то есть!', ui))
fragment_2.add(Phrase('Юуу, в прошлый раз из-за этой фразы мы и оказались в этой ситуации...', tito))
fragment_2.add(Phrase('Да нет же, взгляни, там выход!', ui))
fragment_2.add(Phrase('И в правду!', tito))
fragment_2.add(Phrase('...', avvtor))
fragment_2.add(Phrase('Ну наконец мы выбрались из этого страшного места!', ui))
fragment_2.add(Phrase('Да... Смотри! Это же наш Кеттенкраде', tito))
fragment_2.add(Phrase('Ураааа!', ui))
fragment_2.add(Phrase('Подожди, как мы оказались в том месте?', tito))
fragment_2.add(Phrase('И откуда тут наш транспорт?', tito))
fragment_2.add(Phrase('Это очень странно...', tito))
fragment_2.add(Phrase('Я хочу есть!', ui))
fragment_2.add(Phrase('Знаешь, раз уж мы выбрались после стольких скитаний внури давай сварим супчику! Супчику!!', tito))
fragment_2.add(Phrase('Что ж, но только, чтобы отметить то, что мы выбрались оттуда', tito))
fragment_2.add(Phrase('Ура!!!', ui))
fragment_2.add(Phrase('Но помни, что это из последних запасов', tito))
fragment_2.add(Phrase('МММ... Вкуснатища!', ui))

fragment_1.add(Phrase('Нет!', tito))
fragment_1.add(Phrase('Оууу', ui))
fragment_1.add(Phrase('Надо экономить', tito))
fragment_1.add(Phrase('Но вокруг только тьма непроглядная', ui))
fragment_1.add(Phrase('И поэтому твои глаза должны были к этому привыкнуть', tito))
fragment_1.add(Phrase('Давненько же мы не видели дневного света... интересно сколько времени уже минуло...', ui))
fragment_1.add(Phrase('Я и сама не знаю...', tito))
fragment_1.add(Phrase('', avvtor))

fragment_1.add(Phrase('Любопытно... Где это мы... И почему мы снова оказались в подобном месте?', ui))
fragment_1.add(Phrase('Юуу, скажи...', tito))
fragment_1.add(Phrase('Кто там стенал: "Давай посмотрим, что в той дыре?"... Так ты же, Чии?', ui))
fragment_1.add(Phrase('Нет, это была ты!', tito))
fragment_1.add(Phrase('Что ж... Ты сама сказала тогда...: "Хочу пойти проверить что там"', ui))
fragment_1.add(Phrase('Я и правда так сказала...? В любом случае надо отыскать выход.', tito))
fragment_1.add(Phrase('Да и провианта кот наплакал', ui))
fragment_1.add(Phrase('Ну, еду мы сможем раздобыть если выберемся отсюда', tito))
fragment_1.add(Phrase('Мы даже не знаем, выберемся ли мы вообще', ui))
fragment_1.add(Phrase('Интересно, что же с нами будет. Что скажешь...?', tito))
fragment_1.add(Phrase('Храп...', ui))
fragment_1.add(Phrase('Что ж, пожалуй тоже вздремну...', tito))
fragment_1.add(Phrase('...', ui))
fragment_1.add(Phrase('Kушать...', tito))

fragment_1.add(Phrase('Ммм... Ветер! Рота подъём! Слышь! Юуу!', tito))
fragment_1.add(Phrase('Верно', ui))
fragment_1.add(Phrase('Сейчас свернем и узнаем откуда дует ветер. Думаешь там же и будет выход?', tito))
fragment_1.add(Phrase('Скорей всего', tito))
fragment_1.add(Phrase('Ну, куда?', tito))
fragment_1.add(Phrase('Туда?', tito))

fragment_1.add(Choice(ExampleButton, ('Налево!', '1.1.1'), ('Направо', '1.1.3')))

fragment_3 = Fragment('1.1.3')
fragment_4 = Fragment('1.1.1')

fragment_3.add(Phrase('Направо', ui))
fragment_3.add(Phrase('Блин, Это всего лишь онромный вентилятор...', tito))
fragment_3.add(Phrase('Ну поехали дальше(', ui))
fragment_3.add(Phrase('О, выход!', tito))
fragment_3.add(Phrase('Вот сдорово! Здесь так светло, Чии!', ui))
fragment_3.add(Phrase('... Да, но сейчас ночь на дворе', tito))
fragment_3.add(Phrase('Знаешь, раз уж мы выбрались после стольких скитаний внури давай сварим супчику! Супчику!!', ui))
fragment_3.add(Phrase('Что ж, но только, чтобы отметить то, что мы выбрались оттуда', tito))
fragment_3.add(Phrase('Ура!!!', ui))
fragment_3.add(Phrase('Но помни, что это из последних запасов', tito))
fragment_3.add(Phrase('МММ... Вкуснатища!', ui))

fragment_4.add(Phrase('Поняла', tito))
fragment_4.add(Phrase('Просвет!', ui))

fragment_4.add(Phrase('Вот здорово! Здесь так светло, Тито!', ui))
fragment_4.add(Phrase('... Да, но сейчас ночь на дворе', tito))
fragment_4.add(Phrase('Знаешь, раз уж мы выбрались после стольких скитаний внутри давай сварим супчику! Супчику!!', ui))
fragment_4.add(Phrase('Что ж, но только, чтобы отметить то, что мы выбрались оттуда', tito))
fragment_4.add(Phrase('Ура!!!', ui))
fragment_4.add(Phrase('Но помни, что это из последних запасов', tito))
fragment_4.add(Phrase('Ммм... Вкуснатища!', ui))

'''
fragment.add(Phrase("321", ui, '22'))
fragment.add(Choice(ExampleButton, ('10', '30'), ('20', '30')))

fragment2 = Fragment('30')
fragment2.add(Phrase("3423424", ui))
fragment2.add(Phrase("343242343432423", ui))
'''

plot = compile_plot(fragment, fragment_2, fragment_1, fragment_3, fragment_4)
print(plot)
