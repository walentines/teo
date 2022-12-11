from UI.UIClass import UI
from Tests.testDomain import *
from Tests.testRepository import *
from Tests.testService import *

def start_app():
    ui_class = UI()
    ui_class.run()

test_all_domain()
test_all_repo()
test_all_service()
start_app()