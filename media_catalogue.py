class Movie:
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

class MediaCatalogue:
    def __init__(self):
        self.items = []

    def add(self, media_item):
        self.items.append(media_item)
    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        result = f'Media Catalogue ({len(self.items)} items):\n\n'

        for N, item in enumerate(self.items, start=1):
            result += f'{N}. {item}\n'
        return result
        
try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    movie2 = Movie('The Matrix 2', 2999, 'The Wachowskis', 139)
    
    media_catalogue = MediaCatalogue()
    media_catalogue.add(movie1)
    media_catalogue.add(movie2)

    print(media_catalogue)
except ValueError as e:
    print(f'Validation Error: {e}')