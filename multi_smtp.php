<?php

class multi_smtp extends rcube_plugin {
	public $task = 'mail';
	
	function init(){
		$this->add_hook('smtp_connect', array($this, 'correct_smtp_server'));
        }

	function correct_smtp_server( $data ){
		$imap_server = $_SESSION['storage_host'];
		$data['smtp_server'] = isset($data['smtp_server'][$imap_server]) ? $data['smtp_server'][$imap_server] : array_values($data['smtp_server'])[0];
		//print_r($data);
		return $data;
	}
}

?>
