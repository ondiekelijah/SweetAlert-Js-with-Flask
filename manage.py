def deploy():
	"""Run deployment tasks."""
	from app import app

	app.app_context().push()

	from app import db,User
	
	from flask_migrate import upgrade,migrate,stamp
	db.create_all()
	
	# migrate database to latest revision
	stamp()
	migrate()
	upgrade()
	
deploy()
	