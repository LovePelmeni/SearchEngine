from ..settings import applicationService
import fastapi, json, typing
from ..models import salary
import pydantic
import logging 
from . import exceptions

Logger = logging.getLogger(__name__)

class CustomerSalaryValidationModel(pydantic.BaseModel):
    pass

class JobSalaryPredictionManager(object):
    def predictJobSalary(self, customerNumbers: CustomerSalaryValidationModel):
        pass

@applicationService.post("/upload/job/salary/")
def uploadJobSalary(request: fastapi.Request):
    try:
        requestData = json.loads(request.body)["PredictionNumbers"]
        validatedData = CustomerSalaryValidationModel()
        manager = JobSalaryPredictionManager()
        predictedSalary: int = manager.predictJobSalary()
        return fastapi.Response(content=json.dumps(
        {"predictedSalary": predictedSalary}), status_code=200)

    except(exceptions.SalaryModelException) as exception:
        Logger.error("Failed to Predict the Salary, Exception has been Raised: [%s]" % exception.toString())
        return fastapi.Response(
        content={"Error": exception.toString()}, status_code=400)

@applicationService.get("/get/job/salary/predictions/")
def getJobSalaryPredictions(request: fastapi.Request):
    pass
