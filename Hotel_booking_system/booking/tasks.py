from celery import shared_task
from .models import Booking
from celery import Celery, states
from celery.exceptions import Ignore


'''@shared_task(bind = True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done' '''

@shared_task(bind = True)
def schedule_booking(self, data):
    print(data)
    try:
        get_booking = Booking.objects.get(id = int(data))
        if get_booking:
            get_booking.payment_status = False
            get_booking.save()
            return 'Done'
        
        else:
            self.update_state(
                state = 'FAILURE',
                meta =  {'exe': "Not Found"}
            )
            raise Ignore()

    except:
        self.update_state(
                state = 'FAILURE',
                meta =  {'exe': "Failed"}
            )
        raise Ignore()


