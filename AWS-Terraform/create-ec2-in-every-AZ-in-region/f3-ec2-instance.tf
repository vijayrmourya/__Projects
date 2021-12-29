# EC2 Instance
resource "aws_instance" "ec2_instances" {
  ami                    = data.aws_ami.amzlinux2.id
  instance_type          = var.instance_type
  user_data              = file("${path.module}/f-app1-install.sh")
  key_name               = aws_key_pair.ec2-key-pair.key_name
  vpc_security_group_ids = [aws_security_group.vpc_ssh.id, aws_security_group.vpc_web.id]
  # Create EC2 Instance in all Availabilty Zones of a VPC
  for_each               = toset(keys({
  for az, details in data.aws_ec2_instance_type_offerings.instance-type-list :
  az => details.instance_types if length(details.instance_types) != 0
  }))
  availability_zone      = each.key # You can also use each.value because for list items each.key == each.value
  tags                   = module.global_account_settings.tags
}
