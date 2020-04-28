adjectives_w = ('абсолютный', 'адский', 'азартный', 'активный', 'ангельский', 'антагонистический', 'арктический',
                'астрономический', 'баснословный', 'безапелляционный', 'безбожный', 'безбрежный', 'безвозвратный',
                'безграничный', 'бездонный', 'бездушный', 'безжалостный', 'беззаветный', 'беззастенчивый', 'безмерный',
                'безмятежный', 'безнадежный', 'безоговорочный', 'безотлагательный', 'безраздельный', 'безрассудный',
                'безропотный', 'безудержный', 'безукоризненный', 'безумный', 'безупречный', 'безусловный',
                'безустанный',
                'безутешный', 'безысходный', 'белоснежный', 'бескомпромиссный', 'бесконечный', 'беспардонный',
                'бесповоротный', 'беспощадный', 'беспредельный', 'беспрекословный', 'беспрецедентный', 'беспримерный',
                'беспробудный', 'беспроглядный', 'беспросветный', 'беспросыпный', 'бессовестный', 'бесстыдный',
                'бесценный', 'бесчеловечный', 'бесчисленный', 'бесшабашный', 'бешеный', 'блестящий', 'богатый',
                'богатырский', 'большой', 'буйный', 'бурный', 'варварский', 'великий', 'величайший', 'веский',
                'весомый', 'внушительный', 'возмутительный', 'волчий', 'вопиющий', 'восторженный', 'впечатляющий',
                'всемерный', 'всепоглощающий', 'всесильный', 'всесторонний', 'всяческий', 'выдающийся', 'вылитый',
                'высокий', 'высший', 'галопирующий', 'гибельный', 'гигантский', 'глубокий', 'глубочайший', 'глухой',
                'головокружительный', 'гомерический', 'горький', 'горючий', 'горячий', 'грандиозный', 'гробовой',
                'грозный', 'громадный', 'громкий', 'громоподобный', 'грубый', 'густой', 'диаметральный', 'дивный',
                'дикий', 'добрый', 'доскональный', 'дотошный', 'дремучий', 'душераздирающий', 'дьявольский', 'жаркий',
                'жгучий', 'железный', 'жесткий', 'жестокий', 'жесточайший', 'живой', 'животный', 'жизненный', 'жуткий',
                'завзятый', 'завидный', 'закадычный', 'заклятый', 'законченный', 'закоренелый', 'замечательно',
                'замечательный', 'записной', 'запредельный', 'заядлый', 'звериный', 'зверский', 'зеленый', 'злой',
                'злостный', 'значительный', 'идеальный', 'излишний', 'изрядный', 'изуверский', 'изумительный',
                'исключительный', 'исполинский', 'исступленный', 'истинно', 'истинный', 'истовый', 'истошный',
                'исчерпывающий', 'каменный', 'кардинальный', 'катастрофический', 'категорический', 'клятвенный',
                'колоссальный', 'коренной', 'космический', 'крайний', 'крепкий', 'кристальный', 'кричащий', 'кровный',
                'кромешный', 'круглый', 'крупный', 'крутой', 'леденящий', 'лошадиный', 'лютый', 'максимальный',
                'массовый', 'маститый', 'матерый', 'махровый', 'мертвенно', 'мертвенный', 'мертвецкий', 'мертвый',
                'мировой', 'могильный', 'могучий', 'молниеносный', 'мощный', 'мучительный', 'набитый', 'наглый',
                'наглядный', 'надежный', 'надрывный', 'наибольший', 'наивысший', 'нарочитый', 'настоятельный',
                'настоящий', 'насущный', 'небывалый', 'невероятный', 'невиданный', 'невозможный', 'невообразимый',
                'невосполнимый', 'невыносимый', 'невыразимый', 'недопустимый', 'недосягаемый', 'недюжинный',
                'незабываемый', 'незаурядный', 'неземной', 'неизбывный', 'неизмеримый', 'неимоверный', 'неиссякаемый',
                'неистовый', 'неистощимый', 'неистребимый', 'неисходный', 'неисчерпаемый', 'неисчислимый',
                'немаловажный',
                'немалый', 'немилосердный', 'немой', 'немыслимый', 'ненасытный', 'необоримый', 'необузданный',
                'необыкновенный', 'необычайный', 'неограниченный', 'неодолимый', 'неописуемый', 'неопровержимый',
                'неоспоримый', 'неотразимый', 'неоценимый', 'непередаваемый', 'непереносимый', 'непобедимый',
                'неповторимый', 'непогрешимый', 'неподдельный', 'непоколебимый', 'непомерный', 'непоправимый',
                'непостижимый', 'непревзойденный', 'непреоборимый', 'непреодолимый', 'непререкаемый', 'непримиримый',
                'непробиваемый', 'непробудный', 'непроглядный', 'непролазный', 'непроходимый', 'неразрывный',
                'нерасторжимый', 'несгибаемый', 'несказанный', 'неслыханный', 'несметный', 'несмолкаемый',
                'несмываемый',
                'несокрушимый', 'несравненный', 'нестерпимый', 'несусветный', 'неудержимый', 'неуемный', 'неуклонный',
                'неукоснительный', 'неукротимый', 'неумеренный', 'неустанный', 'неусыпный', 'неутешный', 'неутолимый',
                'неутомимый', 'нечеловеческий', 'нешуточный', 'нещадный', 'обильный', 'обложной', 'образцовый',
                'оглушительный', 'огромный', 'ожесточенный', 'олимпийский', 'ослепительный', 'ослиный', 'основательный',
                'остервенелый', 'острый', 'отборный', 'откровенный', 'открытый', 'отличный', 'отменный', 'отпетый',
                'отчаянный', 'отъявленный', 'ошеломляющий', 'панический', 'патологический', 'первейший',
                'первоклассный',
                'первый', 'пламенный', 'плотный', 'площадной', 'повальный', 'поголовный', 'подавляющий', 'подлинный',
                'подчеркнутый', 'полнейший', 'полный', 'поразительный', 'порядочный', 'последний', 'потрясающий',
                'предельный', 'преклонный', 'преступный', 'приличный', 'принципиальный', 'прирожденный', 'прожженный',
                'проливной', 'пронзительный', 'пронизывающий', 'прямой', 'пущий', 'пьянящий', 'рабский', 'радикальный',
                'разгромный', 'раздирающий', 'разительный', 'разящий', 'райский', 'ревностный', 'революционный',
                'редкий', "термоядерный", "опасный",
                'редкостный', 'резкий', 'рекордный', 'решительный', 'рьяный', 'сатанинский', 'сверхчеловеческий',
                'сверхъестественный', 'свинцовый', 'свирепый', 'седой', 'сердитый', 'серьезный', 'сильный', 'сказочно',
                'сказочный', 'слепой', 'смертельный', 'смертный', 'сногсшибательный', 'собачий', 'совершеннейший',
                'совершенный', 'сокрушительный', 'солидный', 'сплошной', 'стальной', 'стоический', 'стойкий',
                'стопроцентный', 'страстный', 'страшный', 'строгий', 'строжайший', 'сумасшедший', 'суровый',
                'существенный', 'сущий', 'твердый', 'телячий', 'титанический', 'тотальный', 'трескучий', 'триумфальный',
                'тяжелый', 'тяжкий', 'убедительный', 'убежденный', 'убийственный', 'уважительный', 'удивительный',
                'ужасающий', 'ужасный', 'умопомрачительный', 'уничтожающий', 'фанатический', 'фанатичный',
                'фантастический', 'феноменальный', 'филигранный', 'форменный', 'фундаментальный', 'хороший',
                'царский', 'цепенящий', 'черный', 'чертов', 'чертовский', 'чистый', 'чрезвычайный', 'чрезмерный',
                'чудовищный', 'широкий', 'широкомасштабный', 'шквальный', 'штормовой', 'шумный', 'щедрый', 'щемящий',
                'экстраординарный', 'экстремальный', 'ювелирный', 'ядреный', 'яркий', 'яростный', 'ярый')

adjectives_c = (
    "большой", "старый", "громкий", "светлый", "легендарный", "паранормальный", "дефолтный", "широкий", "влажный",
    "тёмный", "тихий", "напряжный", "воздушный", "преступный", "загрезнённый", "непредсказуемый", "спящий", "опасный",
    "радужный", "чужой", "бархатный", "мутный", "ветхий", "сонный", "гиблый", "вздорный", "брюзглый", "медный"
)

nouns_c = (
    "город", "камень", "замок", "посёлок", "участок", "огород", "булыжник", "валун", "холм", "метрополис", "мегаполис",
    "песчаник", "алмаз", "песок", "лагерь", "град", "свод", "склон", "низ"
)

