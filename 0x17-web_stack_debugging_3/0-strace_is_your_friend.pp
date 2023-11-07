# Define an exec resource named 'replace' to run the sed command
exec { 'replace':
  # Specify the command to replace 'phpp' with 'php' in the specified file
  command     => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  # Set refreshonly to true to ensure the command is executed only when triggered by another resource
  refreshonly => true,
}
