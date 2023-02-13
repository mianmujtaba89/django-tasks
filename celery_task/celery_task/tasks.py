from celery import shared_task, states

from time import sleep
from .utils import get_job_completion_percentage


'''
    This task till update the
    status of the cron-job/task 
'''
@shared_task(bind=True)
def my_first_task(self, duration):

    sleep(duration)

    self.update_state(
            state=states.STARTED,
            meta={
                'custom': 'In progress'
            })

    sleep(duration)

    return 'Completed'


'''
    This task till update the progress of the task and also updates the
    status of the cron-job/task 
'''
@shared_task(bind=True)
def progress_task(self, duration):

    try:
        for i in range(60):
            sleep(duration)
            self.update_state(
                state=states.STARTED,
                meta={
                    'pending' : False,
                    'currant' : f"{i+1}",
                    'total' : 60,
                    'percentage' : get_job_completion_percentage(60, i+1),
                    'description' : 'In progress'
                }
            )
        return "Completed"
    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n'),
                'custom': '...'
            })
        raise Ignore()
        return "Failed"