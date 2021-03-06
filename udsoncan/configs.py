default_client_config  = {
	'exception_on_negative_response'	: True,	
	'exception_on_invalid_response'		: True,
	'exception_on_unexpected_response'	: True,
	'security_algo'				: None,
	'security_algo_params'		: None,
	'tolerate_zero_padding' 	: True,
	'ignore_all_zero_dtc' 		: True,
	'dtc_snapshot_did_size' 	: 2,		# Not specified in standard. 2 bytes matches other services format.
	'server_address_format'		: None,		# 8,16,24,32,40
	'server_memorysize_format'	: None,		# 8,16,24,32,40
	'data_identifiers' 			: {},
	'input_output' 				: {}
}
