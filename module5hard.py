from time import sleep


class UrTube:
    def __init__(self, current_user=None):
        self.users = User.user_list
        self.videos = Video.video_list
        self.current_user = current_user

    def log_in(self, nickname, password):
        if len(User.user_list) == 0:
            print(f"Пользователя {nickname} не существует. Пожалуйста зарегистрируйтесь.")
            return
        for i in User.user_list:
            if nickname is i.nickname and hash(password) is i.password:
                self.current_user = i
                print(f'Добро пожаловать {self.current_user.nickname}')
                return self.current_user
            else:
                continue
        print(f"Пользователя {nickname} не существует. Пожалуйста зарегистрируйтесь.")

    def register(self, nickname, password, age):
        if len(User.user_list) == 0:
            nickname = User(nickname, password, age)
            self.current_user = nickname
            print(f'Регистрация {self.current_user.nickname} прошла успешно')
            return self.current_user
        else:
            for i in User.user_list:
                if nickname is i.nickname:
                    print(f"Пользователь {nickname} уже существует. Войдите в учетную запись.")
                    return
            nickname = User(nickname, password, age)
            self.current_user = nickname
            print(f'Регистрация {self.current_user.nickname} прошла успешно')
            return self.current_user

    def log_out(self):
        print(f'Пользователь {self.current_user} вышел из учетной записи')
        self.current_user = None
        return self.current_user

    def add(self, *args):
        for i in args:
            if i not in Video.video_list:
                Video.video_list.append(i)

    def get_videos(self, word):
        video_search = []
        for i in Video.video_list:
            if word.lower() in i.title.lower():
                video_search.append(i.title)
        return video_search

    def watch_video(self, film_title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in Video.video_list:
                if film_title is i.title:
                    if i.adult_mode == True and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for j in range(i.time_now, i.duration + 1):
                            print(j, end=' ')
                            sleep(1)
                        print("Конец видео")


class Video:
    video_list = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.video_list.append(self)


class User:
    user_list = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        User.user_list.append(self)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
