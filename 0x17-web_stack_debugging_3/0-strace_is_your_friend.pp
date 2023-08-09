# This will attempt for fix the 500 error

exec { 'error_fix':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin'],
}
