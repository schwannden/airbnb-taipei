import numpy as np

schema = {
    "id": np.int64,
    "name": object,
    "host_id": np.int64,
    "host_name": object,
    "neighbourhood_group": np.float64,
    "neighbourhood": object,
    "latitude": np.float64,
    "longitude": np.float64,
    "room_type": object,
    "price": np.int64,
    "minimum_nights": np.int64,
    "number_of_reviews": np.int64,
    "last_review": object,
    "reviews_per_month": np.float64,
    "calculated_host_listings_count": np.int64,
    "availability_365": np.int64
}