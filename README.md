# python-wns
Python module for Windows Notification Service (WNS) for Windows tablets/phones(8+)

INSTALL:- 

	pip install python-wns




EXAMPLE:- 

	//Send toast notification
	from python-wns import WNSClient
	token = 'b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87'
	message = {"type": 'toast', "text": ["Hello World!"]}	
	wns = WNSClient('wnsclientid':  '123','wnsclientsecret': 'xyz')
	wns.process(token=token, message=message)
