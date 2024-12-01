import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self._hash_psw(password) #хэширование
        self.age = age
        #print(f'{nickname}, Вы успешно зарегистрировались на UrTube')

    def _hash_psw(self, password):
        return hash(password)

    def __len__(self):
        return self.age

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        print('тут')

    def log_in(self, nickname, password):
        password_hash = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = nickname
                print(f'{user.nickname}, Вы вошли в систему')
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return  #для выхода из метода
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        #print(f'Пользователь {self.current_user} зарегистрировался и вошел в систему')

    def log_out(self):
        print(f'Пользователь {self.current_user} вышел из системы')
        self.current_user = None

    def add(self, *args):
        for arg in args:
            #print(f"Проверка для видео: {arg.title}")
            for video in self.videos:
                if video.title == arg.title:
                    print(f'Видео с названием "{video.title}" уже существует.')
                    break
            else:
                self.videos.append(arg)
                #print(f'Видео "{arg.title} добавлено."')

    def get_videos(self, word):
        search_word = word.lower()
        found_videos = []
        for video in self.videos:
            if search_word in video.title.lower():
                found_videos.append(video.title)
        return found_videos

    def watch_video(self, title_video):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return #завершаем выполнение метода

        for video in self.videos:
            if title_video == video.title: #ищем видео
                if video.adult_mode and len(self.current_user) < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                #print("Начало просмотра")
                while video.time_now <= video.duration:
                    print(video.time_now)
                    video.time_now += 1
                    time.sleep(1)

                print("Конец видео")
                video.time_now = 0
                return

        #print("Видео не найдено")


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
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Проверка log_in
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')