from flask import Flask, render_template, send_from_directory, abort, request, jsonify
from flask_mail import Mail, Message
import os
import logging

app = Flask(__name__, 
            static_url_path='',
            static_folder='.')

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

# Manejador de error 404
@app.errorhandler(404)
def page_not_found(e):
    app.logger.info(f"Página no encontrada: {request.url}")
    return render_template('404.html'), 404

@app.route('/producto/<product_id>')
def product_detail(product_id):
    if product_id not in products:
        app.logger.warning(f"Producto no encontrado: {product_id}")
        abort(404)
    return render_template('product.html', product=products[product_id])

@app.route('/servicio/<service_id>')
def service_detail(service_id):
    if service_id not in services:
        app.logger.warning(f"Servicio no encontrado: {service_id}")
        abort(404)
    return render_template('service.html', service=services[service_id])

# Sample product data - In a real app, this would come from a database
products = {
    'monitores': {
        'name': 'Equipos de Diagnóstico',
        'description': 'Equipos de última generación para diagnósticos precisos y confiables',
        'features': [
            'Alta resolución de imagen',
            'Interfaz intuitiva',
            'Conectividad avanzada',
            'Múltiples modos de visualización'
        ],
        'price': '85,000 MXN',
        'image': 'https://images.unsplash.com/photo-1516549655169-df83a0774514'
    },
    'quirurgicos': {
        'name': 'Instrumentos Quirúrgicos',
        'description': 'Instrumental de alta precisión para procedimientos quirúrgicos',
        'features': [
            'Acero inoxidable de grado médico',
            'Diseño ergonómico',
            'Esterilización garantizada',
            'Kit completo de herramientas'
        ],
        'price': '45,000 MXN',
        'image': 'https://images.unsplash.com/photo-1584362767105-fe6142d68ff3'
    },
    'monitores-medicos': {
        'name': 'Monitores Médicos',
        'description': 'Sistemas de monitorización avanzados para control de pacientes',
        'features': [
            'Monitoreo multiparamétrico',
            'Pantalla táctil HD',
            'Alarmas configurables',
            'Registro de datos continuo'
        ],
        'price': '95,000 MXN',
        'image': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae'
    },
    'equipos-laboratorio': {
        'name': 'Equipos de Laboratorio',
        'description': 'Instrumentos de precisión para análisis clínicos',
        'features': [
            'Alta precisión en resultados',
            'Calibración automática',
            'Sistema de control de calidad',
            'Interfaz de usuario intuitiva'
        ],
        'price': '120,000 MXN',
        'image': 'https://images.unsplash.com/photo-1583912268183-46bf5da946e1'
    },
    'equipos-rehabilitacion': {
        'name': 'Equipos de Rehabilitación',
        'description': 'Tecnología avanzada para terapia física y rehabilitación',
        'features': [
            'Diseño ergonómico',
            'Múltiples niveles de intensidad',
            'Programas personalizables',
            'Monitoreo de progreso'
        ],
        'price': '75,000 MXN',
        'image': 'https://images.unsplash.com/photo-1581594693702-fbdc51b2763b'
    },
    'insumos-medicos': {
        'name': 'Insumos Médicos',
        'description': 'Suministros esenciales para la práctica médica diaria',
        'features': [
            'Alta calidad garantizada',
            'Esterilización certificada',
            'Empaque individual',
            'Disponibilidad inmediata'
        ],
        'price': '25,000 MXN',
        'image': 'https://images.unsplash.com/photo-1584017911766-d451b3d0e843'
    }
}

# Sample services data
services = {
    'mantenimiento': {
        'name': 'Mantenimiento Preventivo',
        'description': 'Servicio técnico especializado para mantener sus equipos médicos en óptimas condiciones',
        'benefits': [
            'Prevención de fallas',
            'Extensión de vida útil del equipo',
            'Optimización del rendimiento',
            'Reducción de costos operativos'
        ],
        'price_from': '2,500 MXN',
        'image': 'https://images.unsplash.com/photo-1581093458791-9f370ac8e0c5',
        'icon': 'fas fa-tools'
    },
    'capacitacion': {
        'name': 'Capacitación Profesional',
        'description': 'Programas de entrenamiento especializado para el uso eficiente de equipos médicos',
        'benefits': [
            'Certificación profesional',
            'Prácticas hands-on',
            'Material didáctico actualizado',
            'Instructores certificados'
        ],
        'price_from': '5,000 MXN',
        'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d',
        'icon': 'fas fa-graduation-cap'
    },
    'soporte': {
        'name': 'Soporte de Emergencia',
        'description': 'Asistencia técnica 24/7 para resolver problemas críticos con sus equipos médicos',
        'benefits': [
            'Disponibilidad 24/7',
            'Respuesta inmediata',
            'Soporte remoto y presencial',
            'Soluciones rápidas y efectivas'
        ],
        'price_from': '3,500 MXN',
        'image': 'https://images.unsplash.com/photo-1582213782179-e0d53f982ca?',
        'icon': 'fas fa-ambulance'
    },
    'instalacion': {
        'name': 'Instalación',
        'description': 'Servicio profesional de montaje y configuración de equipos médicos',
        'benefits': [
            'Instalación certificada',
            'Configuración personalizada',
            'Pruebas de funcionamiento',
            'Capacitación básica incluida'
        ],
        'price_from': '4,500 MXN',
        'image': 'https://images.unsplash.com/photo-1581093458791-9f370ac8e0c5',
        'icon': 'fas fa-cogs'
    },
    'certificacion': {
        'name': 'Certificación',
        'description': 'Servicios de validación y certificación de equipos médicos',
        'benefits': [
            'Certificación oficial',
            'Documentación completa',
            'Pruebas exhaustivas',
            'Reporte detallado'
        ],
        'price_from': '6,000 MXN',
        'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d',
        'icon': 'fas fa-clipboard-check'
    },
    'actualizacion': {
        'name': 'Actualización',
        'description': 'Servicio de modernización y actualización de equipos existentes',
        'benefits': [
            'Mejora de rendimiento',
            'Actualización de software',
            'Compatibilidad garantizada',
            'Mínimo tiempo de inactividad'
        ],
        'price_from': '7,500 MXN',
        'image': 'https://images.unsplash.com/photo-1582213782179-e0d53f982ca?',
        'icon': 'fas fa-sync'
    }
}

# Agregar nuevos cursos al diccionario existente
courses = {
    'ecografia-basica': {
        'name': 'Ecografía Básica',
        'description': 'Curso introductorio a la ecografía médica',
        'benefits': [
            'Fundamentos de ultrasonido',
            'Práctica con equipos modernos',
            'Certificación avalada',
            'Material didáctico incluido'
        ],
        'price': '15,000 MXN',
        'duration': '40 horas',
        'start_date': '15 de Abril, 2025',
        'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d',
        'icon': 'fas fa-heartbeat'
    },
    'radiologia-digital': {
        'name': 'Radiología Digital',
        'description': 'Especialización en interpretación de imágenes radiológicas digitales',
        'benefits': [
            'Tecnologías de imagen digital',
            'Casos clínicos prácticos',
            'Software especializado',
            'Evaluación continua'
        ],
        'price': '18,000 MXN',
        'duration': '60 horas',
        'start_date': '1 de Mayo, 2025',
        'image': 'https://images.unsplash.com/photo-1583912268183-46bf5da946e1',
        'icon': 'fas fa-x-ray'
    },
    'equipos-medicos': {
        'name': 'Manejo de Equipos Médicos',
        'description': 'Capacitación integral en operación de equipos médicos avanzados',
        'benefits': [
            'Operación segura',
            'Mantenimiento preventivo',
            'Protocolos de seguridad',
            'Prácticas supervisadas'
        ],
        'price': '12,000 MXN',
        'duration': '30 horas',
        'start_date': '10 de Mayo, 2025',
        'image': 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae',
        'icon': 'fas fa-cogs'
    },
    'ultrasonido-cardiaco': {
        'name': 'Ultrasonido Cardíaco',
        'description': 'Especialización en ecocardiografía y diagnóstico cardíaco',
        'benefits': [
            'Técnicas avanzadas de ultrasonido',
            'Interpretación de imágenes cardíacas',
            'Casos clínicos especializados',
            'Certificación internacional'
        ],
        'price': '20,000 MXN',
        'duration': '80 horas',
        'start_date': '20 de Mayo, 2025',
        'image': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118',
        'icon': 'fas fa-heart'
    },
    'resonancia-magnetica': {
        'name': 'Resonancia Magnética',
        'description': 'Formación especializada en tecnología de resonancia magnética',
        'benefits': [
            'Principios físicos de RM',
            'Protocolos de adquisición',
            'Optimización de imágenes',
            'Seguridad del paciente'
        ],
        'price': '25,000 MXN',
        'duration': '100 horas',
        'start_date': '5 de Junio, 2025',
        'image': 'https://images.unsplash.com/photo-1516549655169-df83a0774514',
        'icon': 'fas fa-magnet'
    },
    'tomografia-computarizada': {
        'name': 'Tomografía Computarizada',
        'description': 'Curso avanzado en TC multicorte y reconstrucción 3D',
        'benefits': [
            'Técnicas de adquisición 3D',
            'Reconstrucción multiplanar',
            'Protocolos específicos',
            'Casos clínicos avanzados'
        ],
        'price': '22,000 MXN',
        'duration': '90 horas',
        'start_date': '15 de Junio, 2025',
        'image': 'https://images.unsplash.com/photo-1584362767105-fe6142d68ff3',
        'icon': 'fas fa-cube'
    }
}

# Agregar la nueva ruta para cursos
@app.route('/curso/<course_id>')
def course_detail(course_id):
    if course_id not in courses:
        app.logger.warning(f"Curso no encontrado: {course_id}")
        abort(404)
    return render_template('course.html', course=courses[course_id])

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/privacy')
def privacy():
    return send_from_directory('.', 'privacy.html')


# Nueva ruta para procesar el formulario de contacto
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        data = request.form
        name = data.get('name')
        email = data.get('email')
        area = data.get('area')
        message = data.get('message')

        # Validación básica
        if not all([name, email, area, message]):
            return jsonify({'success': False, 'message': 'Por favor complete todos los campos'}), 400

        # Crear el mensaje de correo
        msg_body = f"""
        Nuevo mensaje de contacto:

        Nombre: {name}
        Email: {email}
        Área de interés: {area}
        Mensaje: {message}
        """

        msg = Message(
            subject='Nuevo mensaje de contacto - Biomectech',
            recipients=[os.environ.get('MAIL_USERNAME')],  # Usar el mismo correo como destinatario
            body=msg_body
        )

        # Logging para debug
        app.logger.info(f"Intentando enviar correo a: {os.environ.get('MAIL_USERNAME')}")

        mail.send(msg)

        return jsonify({
            'success': True,
            'message': 'Mensaje enviado correctamente. Nos pondremos en contacto pronto.'
        })

    except Exception as e:
        app.logger.error(f"Error en el formulario de contacto: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Hubo un error al enviar el mensaje. Por favor intente más tarde.'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)