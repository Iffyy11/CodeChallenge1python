class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        
        return self._author
    
    @author.setter
    def author(self, author_name):
        if not isinstance(author_name, Author):
            raise Exception("Author must be an Author instance.")
        self._author = author_name

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine_name):
        if not isinstance(magazine_name, Magazine):
            raise Exception("Magazine must be a Magazine instance.")
        self._magazine = magazine_name

    @property
    def title(self):
        
        return self._title
    
    @title.setter
    def title(self, title_name):
        if not isinstance(title_name, str):
            raise Exception("Title must be a string.")
        if not (5 <= len(title_name) <= 50):
            raise Exception('Titles must be between 5 and 50 characters, inclusive.')
        if hasattr(self, "_title"):
            raise Exception("Title cannot be changed.")
        
        self._title = title_name



class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("The name should be a string!")
        if len(name.strip()) == 0:
            raise Exception("The name should not be empty.")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.magazines():
            return None
        return list(set(magazine.category for magazine in self.magazines()))



class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, mag_name):
        if not isinstance(mag_name, str):
            raise Exception("Names must be of type str.")
        if not (2 <= len(mag_name) <= 16):
            raise Exception("Names must be between 2 and 16 characters, inclusive.")
        self._name = mag_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a non-empty string.")
        if len(value.strip()) == 0:
            raise Exception("Category must be non-empty.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))


if __name__ == "__main__":
    # Create Authors
    author1 = Author("Ifra")
    author2 = Author("Hafifa")

    # Create Magazines
    mag1 = Magazine("TechToday", "Technology")
    mag2 = Magazine("HealthLife", "Health")

    # Add Articles
    article1 = Article(author1, mag1, "The Future of AI")
    article2 = Article(author2, mag1, "Cybersecurity Trends")
    article3 = Article(author1, mag2, "Healthy Living Tips")
    article4 = Article(author1, mag1, "AI in Everyday Life")

    # Print some outputs
    print("Author1 articles:", [a.title for a in author1.articles()])
    print("Magazine1 contributors:", [a.name for a in mag1.contributors()])
    print("Magazine1 article titles:", mag1.article_titles())
    print("Magazine1 contributing authors:", [a.name for a in mag1.contributing_authors()] if mag1.contributing_authors() else None)
    print("Top publisher:", Magazine.top_publisher().name)

