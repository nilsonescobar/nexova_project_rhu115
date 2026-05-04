from django.shortcuts import render
from django.contrib.auth.decorators import login_required

NAV_ITEMS = [
    {'name': 'home',         'url': '/home/',         'label': 'Inicio'},
    {'name': 'empleados',    'url': '/empleados/',    'label': 'Empleados'},
    {'name': 'prestaciones', 'url': '/prestaciones/', 'label': 'Prestaciones'},
    {'name': 'ausencias',    'url': '/ausencias/',    'label': 'Ausencias'},
]


MODULES = [
    {
        'title':       'Empleados',
        'description': 'Registro, consulta y administración del personal activo e inactivo de la empresa.',
        'url':         '/empleados/',
        'icon':        '👥',
        'color':       'blue',
        'status':      'En desarrollo',
        'status_type': 'dev',
        'tags':        ['Registro', 'Consulta', 'Edición', 'Historial'],
    },
    {
        'title':       'Prestaciones y Planilla',
        'description': 'Cálculo automático de cuotas patronales, planilla mensual y generación de boletas.',
        'url':         '/prestaciones/',
        'icon':        '💰',
        'color':       'amber',
        'status':      'En desarrollo',
        'status_type': 'dev',
        'tags':        ['ISSS', 'AFP', 'Aguinaldo', 'Vacaciones', 'Boleta'],
    },
    {
        'title':       'Ausencias e Incapacidades',
        'description': 'Control de ausencias, incapacidades y descuentos aplicados a planilla mensual.',
        'url':         '/ausencias/',
        'icon':        '📋',
        'color':       'green',
        'status':      'En desarrollo',
        'status_type': 'dev',
        'tags':        ['Ausencias', 'Incapacidades', 'Descuentos', 'Reportes'],
    },
]

STATS = [
    {'label': 'Empleados activos', 'value': '—', 'sub': 'Por configurar'},
    {'label': 'Planillas del año', 'value': '0', 'sub': 'Generadas'},
    {'label': 'Ausencias del mes', 'value': '0', 'sub': 'Registradas'},
    {'label': 'Incapacidades',     'value': '0', 'sub': 'Activas'},
]

LEGAL_ITEMS = [
    {'title': 'Código de Trabajo de El Salvador',
     'description': 'Base legal para vacaciones, aguinaldo y prestaciones laborales.'},
    {'title': 'Reforma laboral octubre 2025',
     'description': 'Fecha de corte 12 de diciembre para aguinaldo proporcional.'},
    {'title': 'ISSS — Cuota patronal 7.5%',
     'description': 'Aplicada sobre salario máximo de referencia de $1,000.00.'},
    {'title': 'AFP — Cuota patronal 8.75%',
     'description': 'Sin tope salarial según reforma previsional 2025.'},
    {'title': 'INSAFORP — 1%',
     'description': 'Aplica a empresas con diez o más empleados.'},
]

QUICK_ACTIONS = [
    {'label': 'Registrar empleado',       'description': 'Agregar un nuevo colaborador al sistema', 'icon': '➕', 'url': '/empleados/'},
    {'label': 'Generar planilla del mes', 'description': 'Procesar la planilla del período actual', 'icon': '📄', 'url': '/prestaciones/'},
    {'label': 'Registrar ausencia',       'description': 'Ingresar una ausencia o incapacidad',     'icon': '📝', 'url': '/ausencias/'},
]

MODULE_FEATURES = {
    'empleados': {
        'page_title':       'Empleados',
        'page_subtitle':    'Gestión del personal de Nexova Business Group',
        'breadcrumb':       'Módulo de empleados',
        'module_icon':      '👥',
        'planned_features': [
            'Registro de nuevos empleados con información completa',
            'Consulta y búsqueda avanzada del personal',
            'Edición de datos personales y laborales',
            'Activación y desactivación de colaboradores',
            'Historial laboral por empleado',
        ],
    },
    'prestaciones': {
        'page_title':       'Prestaciones y Planilla',
        'page_subtitle':    'Cálculo de planillas y generación de boletas de pago',
        'breadcrumb':       'Módulo de prestaciones',
        'module_icon':      '💰',
        'planned_features': [
            'Cálculo de cuotas ISSS, AFP e INSAFORP por empleado',
            'Generación de planilla mensual completa',
            'Cálculo de aguinaldo según antigüedad y reforma 2025',
            'Cálculo de vacaciones con recargo del 30% (Art. 177)',
            'Impresión de boleta de pago individual',
        ],
    },
    'ausencias': {
        'page_title':       'Ausencias e Incapacidades',
        'page_subtitle':    'Registro y control de ausencias del personal',
        'breadcrumb':       'Módulo de ausencias',
        'module_icon':      '📋',
        'planned_features': [
            'Registro de ausencias justificadas e injustificadas',
            'Control de incapacidades con subsidio del ISSS',
            'Cálculo automático de descuentos en planilla',
            'Historial de ausencias por empleado',
            'Reportes mensuales de ausentismo',
        ],
    },
}


def _ctx(extra=None):
    ctx = {'nav_items': NAV_ITEMS}
    if extra:
        ctx.update(extra)
    return ctx


@login_required
def home(request):
    return render(request, 'core/home.html', _ctx({
        'modules':       MODULES,
        'stats':         STATS,
        'legal_items':   LEGAL_ITEMS,
        'quick_actions': QUICK_ACTIONS,
    }))


@login_required
def empleados(request):
    return render(request, 'core/coming_soon.html', _ctx(MODULE_FEATURES['empleados']))


@login_required
def prestaciones(request):
    return render(request, 'core/coming_soon.html', _ctx(MODULE_FEATURES['prestaciones']))


@login_required
def ausencias(request):
    return render(request, 'core/coming_soon.html', _ctx(MODULE_FEATURES['ausencias']))