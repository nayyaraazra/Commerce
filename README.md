# Commerce

This is an online auction web app built with Django, created as part of the CS50W course.

The idea is similar to eBay: anyone can put up an item for auction, other users can place bids on it, and when the owner decides to close the auction, the highest bidder wins.

---

## What You Can Do

- **Register / Log in** — create an account to start using the site
- **Create a listing** — post an item with a title, description, starting price, optional image, and category
- **Place a bid** — bid on any active listing (your bid must be higher than the current highest bid)
- **Watchlist** — save listings you're interested in so you can find them easily later
- **Comments** — leave a comment on any listing
- **Close an auction** — if you created the listing, you can close it at any time; the highest bidder at that point is declared the winner
- **Browse by category** — filter listings by category to find what you're looking for
- **Admin panel** — site administrators can manage all listings, bids, users, and comments through Django's built-in admin interface

---

## How to Run It Locally

Make sure you have Python and Django installed, then follow these steps:

```bash
# Step 1: Install required packages
pip install -r requirements.txt

# Step 2: Set up the database
python manage.py migrate

# Step 3: (Optional) Create an admin account
python manage.py createsuperuser

# Step 4: Start the server
python manage.py runserver
```
---

## Project Structure

```
commerce/
├── auctions/               # Main app — all the auction logic lives here
│   ├── migrations/         # Database migration history
│   ├── templates/auctions/ # HTML templates for each page
│   ├── admin.py            # Admin panel configuration
│   ├── models.py           # Database models (User, Listing, Bid, etc.)
│   ├── urls.py             # URL routes for the app
│   └── views.py            # Page logic and form handling
├── commerce/               # Project-level configuration
│   ├── settings.py         # Django settings (database, media, installed apps)
│   └── urls.py             # Root URL configuration
└── manage.py               # Django's command-line utility
```

---

## Database Models

| Model | What it represents |
|---|---|
| **User** | A registered user. Built on top of Django's default user system. |
| **AuctionList** | A single auction listing — includes title, description, starting bid, image, category, and who won. |
| **Bid** | A bid placed by a user on a specific listing, with the bid amount recorded. |
| **Comment** | A comment left by a user on a listing. |
| **Category** | A label used to group listings (e.g. Electronics, Clothing). |
