from abc import ABC, abstractmethod

class BaseAdapter(ABC):
   """
   Abstract base class (Target) defining the interface all AI model adapters must implement.
   """
   
   @abstractmethod
   def generate_boolean_query(self, job_description: str, industry: str) -> str:
       """
        Generate a recruiter-grade Boolean search string
        from a job description and industry.
        
        :param jd_text: The job description text.
        :param industry: The classified industry domain (e.g., IT, Healthcare).
        :return: A formatted Boolean query string.
        """
       pass
   