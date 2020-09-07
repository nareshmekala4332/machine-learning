from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from datetime import datetime

import logging
import requests
import json
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

logger = logging.getLogger(__name__)

#class ApiAction(Action):
#	def name(self):
#	   return "action_match_news"
#
#	def run(self, dispatcher, tracker, domain):
#		res = requests.get(API_URL + "matches" + "?apikey=" + API_KEY)
#		if res.status_code == 200:
#			data = res.json()["matches"]
#			recent_match = data[0]
#			upcoming_match = data[1]
#			upcoming_match["date"] = datetime.strptime(upcoming_match["date"], "%Y-%m-%dT%H:%M:%S.%fZ")
#			next_date = upcoming_match["date"].strftime("%d %B %Y")
#
#			out_message = "Here some IPL quick info:\n1.The match between {} and {} was recently held and {} won.".format(recent_match["team-1"], recent_match["team-2"], recent_match["winner_team"])
#
#			dispatcher.utter_message(out_message)
#
#			out_message = "2.The next match is {} vs {} on {}".format(upcoming_match["team-1"], upcoming_match["team-2"], next_date)
#
#			dispatcher.utter_message(out_message)
#
#		return [] 
#-->

class FacilitiesByCustomerAction(Action):

    def name(self) -> Text:
        return "action_facility_enquiry_custid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(str(tracker.latest_message['text']))
        dispatcher.utter_message(text="Your Facilities: \n Facility Id: 50000010 \t Name: Facility1 \n Facility Id: 50000011 \t Name: Facility2\n Facility Id: 50000012 \t Name: Facility3")

        return []
		
class FacilitiesByFacilityIDAction(Action):

    def name(self) -> Text:
        return "action_facility_enquiry_facid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
			
        print(str(tracker.latest_message['text']))
        dispatcher.utter_message(text="Your Facilities: \n Facility Id: 50000010 \t Name: Facility1 \n Amount: 10000000 \t Currency: USD \n Facility Type: Termc \t Facility Description: Fac Terms")

        return []	
class LoansByCustomerAction(Action):

    def name(self) -> Text:
        return "action_loans_enquiry_custid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(str(tracker.latest_message['text']))
        dispatcher.utter_message(text="Your Loans: \n Loan Id: 60000010 \t Name: Loan1 \n Loan Id: 50000011 \t Name: Loan2\n Loan Id: 50000012 \t Name: Loan3")

        return []
class LoansByFacilityIDAction(Action):

    def name(self) -> Text:
        return "action_loans_enquiry_facid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your Loans: \n Loan Id: 60000010 \t Name: Loan1 \n Amount: 500000 \t Currency: USD\n EffectiveDate: 2020-02-06 \t MaturityDate: 2029-02-06")

        return []   
		
class StatementsByCustomerAction(Action):

    def name(self) -> Text:
        return "action_stat_enquiry_custid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your Statements: \n Id: 70000010 \t Name: Statement 1 \n Link: PDF Link to download Statement 1 \t Id: 70000011\n Name : Statement 2 \t Link : PDF Link to download Statement 2 ")

        return []

class StatementsByFacilityAction(Action):

    def name(self) -> Text:
        return "action_stat_enquiry_facid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your Statements: \n Id: 70000010 \t Name: Statement 1 \n Link: PDF Link to download Statement 1")

        return []

class PaymentsByCustomerAction(Action):

    def name(self) -> Text:
        return "action_payments_enquiry_custid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your Payments: \n Id: 80000010 \t Description: Payment descrp 1 \n Invoice Status: Due  \t Id: 80000011\n Description : Payment descrp 2 \t Invoice Status : Due ")

        return []

class PaymentsByFacilityAction(Action):

    def name(self) -> Text:
        return "action_payments_enquiry_facid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your Payments: \n Id: 80000010 \t Description: Payment descrp 1 \n Invoice Status: Due ")

        return []

class PaymentsByLoanAction(Action):

    def name(self) -> Text:
        return "action_payments_enquiry_loanid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your Payments: \n Id: 80000010 \t Description: Payment descrp 1 \n Invoice Status: Due ")

        return []