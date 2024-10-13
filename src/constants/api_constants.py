# API Constants - Class which contains all endpoints
# Keep the URLs

class APIConstants(Object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"


    # UPDATE -> PUT,PATCH,UPDATE,DELETE -> using bookingId
    def url_put_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)