# 📊 Análisis de Datos de Estudiantes con Python

## 🎯 Descripción del Proyecto

Este proyecto implementa un análisis completo de datos de estudiantes utilizando Python y metodología CRISP-DM. El objetivo es responder preguntas clave sobre el rendimiento académico y identificar factores que influyen en el éxito estudiantil.

## 📋 Objetivos

El análisis busca responder **5 preguntas fundamentales**:

1. **¿Cuáles son los factores que influyen en el rendimiento de los estudiantes?**
2. **¿Cuáles son los temas que mejor dominan los estudiantes?**
3. **¿Cuáles son los temas que peor rendimiento registran los estudiantes?**
4. **¿Cuál es el GPA promedio de los estudiantes y qué factores influencian el resultado?**
5. **¿Qué estudiantes obtienen mejor desempeño según su género?**

## 🔬 Metodología

El proyecto utiliza la metodología **CRISP-DM** (Cross Industry Standard Process for Data Mining):

1. **Comprensión del negocio** - Definición de objetivos y problemas a resolver
2. **Comprensión de los datos** - Exploración y análisis de calidad de datos
3. **Preparación de los datos** - Limpieza y transformación
4. **Modelado** - Aplicación de técnicas estadísticas y de machine learning
5. **Evaluación** - Validación de resultados
6. **Despliegue** - Documentación y presentación de findings

## 📁 Estructura del Proyecto

```
Student-Data-Analysis-with-Python/
│
├── data/
│   └── students_data.csv           # Dataset de estudiantes
│
├── student-data-analysis.ipynb     # Notebook principal con análisis completo
├── README.md                       # Documentación del proyecto
└── .gitignore                      # Archivos a excluir del control de versiones
```

## 📊 Dataset

El dataset contiene **105 registros** de estudiantes con **14 variables**:

### Variables del Dataset:
- **Student_ID**: Identificador único del estudiante
- **gender**: Género del estudiante (female/male)
- **from1, from2, from3**: Calificaciones categóricas (A, B, C)
- **Algebra**: Calificación en Álgebra (0-100)
- **Calculus1**: Calificación en Cálculo I (0-100)
- **Calculus2**: Calificación en Cálculo II (0-100)
- **Statistics**: Calificación en Estadística (0-100)
- **Probability**: Calificación en Probabilidad (0-100)
- **Measure**: Calificación en Teoría de la Medida (0-100)
- **Functional_analysis**: Calificación en Análisis Funcional (0-100)
- **GPA**: Grade Point Average - Promedio General (0-100)
- **Attendance**: Porcentaje de asistencia (0-100)

## 🛠️ Tecnologías Utilizadas

- **Python 3.11+**
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Computación numérica
- **Matplotlib** - Visualización de datos
- **Seaborn** - Visualización estadística
- **Scikit-learn** - Machine learning y modelado
- **SciPy** - Análisis estadístico
- **Jupyter Notebook** - Ambiente de desarrollo interactivo

## 🚀 Instalación y Uso

### Prerrequisitos
```bash
Python 3.8 o superior
pip (gestor de paquetes de Python)
```

### Instalación
1. **Clona el repositorio:**
```bash
git clone https://github.com/Jesus-David-Silva-Rangel-19/Student-Data-Analysis-with-Python.git
cd Student-Data-Analysis-with-Python
```

2. **Instala las dependencias:**
```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy jupyter
```

3. **Ejecuta el notebook:**
```bash
jupyter notebook student-data-analysis.ipynb
```

## 📈 Principales Hallazgos

### 🎯 Factores Clave que Influyen en el Rendimiento:
- **Asistencia**: Correlación significativa con el GPA
- **Statistics**: Materia con mayor correlación con rendimiento general
- **Probability**: Segunda materia más influyente
- **Género**: Ligera ventaja en estudiantes femeninas

### 📚 Materias Mejor Dominadas:
1. **Statistics** (promedio más alto)
2. **Probability** 
3. **Measure**

### ⚠️ Materias que Requieren Atención:
1. **Functional_analysis** (promedio más bajo)
2. **Calculus1**
3. **Calculus2**

### 👥 Análisis por Género:
- **Participación**: 65% mujeres, 35% hombres
- **Rendimiento**: Ligera ventaja de estudiantes femeninas
- **Distribución**: Rendimiento similar en la mayoría de materias

## 📊 Visualizaciones Incluidas

- Distribuciones de calificaciones por materia
- Matriz de correlación entre variables
- Análisis comparativo por género
- Boxplots y histogramas de rendimiento
- Gráficos de dispersión GPA vs. materias
- Análisis de asistencia vs. rendimiento

## 🔍 Análisis Estadístico

- **Estadística descriptiva** completa
- **Análisis de correlación** entre variables
- **Tests de significancia** estadística
- **Modelos de regresión lineal** para predicción
- **Análisis multivariado** de factores

## 💡 Recomendaciones

### Para Instituciones Educativas:
1. **Enfoque en materias desafiantes** - Reforzar Análisis Funcional y Cálculo
2. **Promoción de asistencia** - Implementar incentivos y seguimiento
3. **Aprovechamiento de fortalezas** - Usar Statistics como materia modelo
4. **Equidad de género** - Mantener igualdad de oportunidades
5. **Monitoreo continuo** - Sistema de seguimiento académico

### Para Estudiantes:
1. Mantener **asistencia regular** a clases
2. Dedicar tiempo extra a **materias desafiantes**
3. Aprovechar **fortalezas** en Statistics y Probability
4. Participar en **grupos de estudio** y tutorías

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Contacto

**Jesús David Silva Rangel**
- GitHub: [@Jesus-David-Silva-Rangel-19](https://github.com/Jesus-David-Silva-Rangel-19)
- Email: [contacto disponible en perfil de GitHub]

## 🙏 Agradecimientos

- Metodología CRISP-DM para análisis estructurado
- Comunidad de Python y librerías de ciencia de datos
- Kaggle por inspiración en estructura de datasets educativos

---

⭐ **¡Si te gusta este proyecto, dale una estrella!** ⭐
