class CookieListing:
    """
    Cookie Object

    You can buy these
    """

    def __init__(self, id, name, description, price, image):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image


cookies_listings = [
    CookieListing(
        0, "12x Cookies", "Enough for small gatherings", 20, "cookies_12.png"
    ),
    CookieListing(1, "24x Cookies", "Can't go wrong with 24", 37.5, "cookies_24.png"),
    CookieListing(2, "36x Cookies", "Enough for a full party", 50, "cookies_36.png"),
]
