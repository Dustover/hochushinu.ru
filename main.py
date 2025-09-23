import pandas as pd
import os
from pathlib import Path
import re

# Шаблон HTML страницы
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="ru">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{title} - Хочу Шину!</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">

  <!-- Favicons -->
  <link href="../assets/img/favicon.png" rel="icon">
  <link href="../assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="../assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="../assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="../assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Main CSS File -->
  <link href="../assets/css/main.css" rel="stylesheet">

  <!-- Дополнительные стили для страниц товаров -->
  <link href="../assets/css/product-pages.css" rel="stylesheet">

  <!-- =======================================================
  * Template Name: MyPortfolio
  * Template URL: https://bootstrapmade.com/myportfolio-bootstrap-portfolio-website-template/
  * Updated: Aug 08 2024 with Bootstrap v5.3.3
  * Author: BootstrapMade.com
  * License: https://bootstrapmade.com/license/
  ======================================================== -->
</head>

<body class="portfolio-details-page">

  <header id="header" class="header d-flex align-items-center sticky-top">
    <div class="container-fluid  position-relative d-flex align-items-center justify-content-between">

      <a href="../index.html" class="logo d-flex align-items-center">
        <h1 class="sitename">Хочу Шину!</h1>
      </a>

      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="../index.html">Домой</a></li>
          <li><a href="../about.html">О нас</a></li>
          <li><a href="../contact.html">Контакты</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>

    </div>
  </header>

  <main class="main">

    <!-- Page Title -->
    <div class="page-title light-background">
      <div class="container">
        <h1>{name}</h1>
        <nav class="breadcrumbs">
          <ol>
            <li><a href="../index.html">Домой</a></li>
            <li><a href="../index.html#{category_id}">{category_name}</a></li>
            <li class="current">{name}</li>
          </ol>
        </nav>
      </div>
    </div><!-- End Page Title -->

    <!-- Portfolio Details Section -->
    <section id="portfolio-details" class="portfolio-details section">

      <div class="container" data-aos="fade-up" data-aos-delay="100">

        <div class="row gy-4">

          <div class="col-lg-8">
            <div class="portfolio-details-slider swiper">
              <div class="swiper-wrapper align-items-center">
                {image_slides}
              </div>
              <div class="swiper-pagination"></div>
            </div>

            <!-- Превью изображений -->
            <div class="thumbnail-slider swiper mt-3">
              <div class="swiper-wrapper">
                {thumbnail_slides}
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="portfolio-info" data-aos="fade-up" data-aos-delay="200">
              <h3>Информация о шине</h3>
              <ul>
                <li><strong>Бренд</strong>: {brand}</li>
                <li><strong>Модель</strong>: {model}</li>
                <li><strong>Категория</strong>: {subcategory}</li>
                <li><strong>Размер</strong>: {width}/{height}R{diameter}</li>
                <li><strong>Индекс нагрузки</strong>: {load_index}</li>
                <li><strong>Цена</strong>: {price_formatted} руб.</li>
                <li><strong>Артикул</strong>: {sku}</li>
              </ul>
            </div>
            <div class="portfolio-description" data-aos="fade-up" data-aos-delay="300">
              <h2>Описание</h2>
              <p>{full_description}</p>

              <!-- Кнопка WhatsApp после описания -->
              <div class="whatsapp-btn-container mt-4" data-aos="fade-up" data-aos-delay="400">
                <a href="https://wa.me/79211813093?text=Здравствуйте! Интересует {name}" 
                   class="whatsapp-btn" 
                   target="_blank">
                  <i class="bi bi-whatsapp"></i>
                  Заказать по WhatsApp
                </a>
              </div>
            </div>
          </div>

        </div>

      </div>

    </section><!-- /Portfolio Details Section -->

  </main>

  <footer id="footer" class="footer light-background">

    <div class="container">
      <div class="copyright text-center ">
        <p>© <span>Copyright</span> <strong class="px-1 sitename">Хочу Шину!</strong> <span>All Rights Reserved</span></p>
      </div>
      <div class="social-links d-flex justify-content-center">
        <a href="tel:+79211813093"><i class="bi bi-phone"></i></a>
        <a href="mailto:monogarov.simbiom@yandex.ru"><i class="bi bi-envelope"></i></a>
      </div>
      <div class="credits">
        Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
      </div>
    </div>

  </footer>

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Preloader -->
  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="../assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/vendor/php-email-form/validate.js"></script>
  <script src="../assets/vendor/aos/aos.js"></script>
  <script src="../assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="../assets/vendor/imagesloaded/imagesloaded.pkgd.min.js"></script>
  <script src="../assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="../assets/vendor/swiper/swiper-bundle.min.js"></script>

  <!-- Main JS File -->
  <script src="../assets/js/main.js"></script>

  <script>
    // Скрипт для связи основного слайдера с превью
    document.addEventListener('DOMContentLoaded', function() {{
      // Инициализация слайдера миниатюр
      var thumbnailSlider = new Swiper('.thumbnail-slider', {{
        slidesPerView: 4,
        spaceBetween: 10,
        freeMode: true,
        watchSlidesProgress: true,
        breakpoints: {{
          320: {{ slidesPerView: 3 }},
          480: {{ slidesPerView: 4 }},
          768: {{ slidesPerView: 5 }},
          992: {{ slidesPerView: 6 }}
        }}
      }});

      // Инициализация основного слайдера
      var mainSlider = new Swiper('.portfolio-details-slider', {{
        loop: true,
        speed: 600,
        autoplay: {{ delay: 5000 }},
        slidesPerView: 1,
        pagination: {{ 
          el: '.swiper-pagination', 
          type: 'bullets',
          clickable: true 
        }},
        thumbs: {{
          swiper: thumbnailSlider
        }}
      }});

      // Добавляем активный класс для миниатюр
      thumbnailSlider.on('click', function (swiper, event) {{
        var clickedIndex = swiper.clickedIndex;
        mainSlider.slideTo(clickedIndex);
      }});
    }});
  </script>

</body>

</html>'''


def format_price(price):
    """Форматирование цены с пробелами"""
    return f"{int(price):,}".replace(",", " ")


def get_category_id(subcategory):
    """Получить ID категории для ссылок"""
    category_map = {
        'Сельскохозяйственные': 'agricultural',
        'Грузовые': 'truck',
        'Легкогрузовые': 'app-light-trucks'
    }
    return category_map.get(subcategory, 'portfolio')


def get_category_name(subcategory):
    """Получить русское название категории"""
    category_map = {
        'Сельскохозяйственные': 'Сельскохозяйственные шины',
        'Грузовые': 'Грузовые шины',
        'Легкогрузовые': 'Легкогрузовые шины'
    }
    return category_map.get(subcategory, 'Шины')


def extract_image_urls(html_content):
    """Извлекает URL изображений из HTML-строки."""
    if pd.isna(html_content) or not html_content:
        return ""

    # Используем регулярное выражение для поиска всех URL в атрибуте src
    pattern = r'<img[^>]*src="([^"]*)"[^>]*>'
    matches = re.findall(pattern, html_content)

    # Возвращаем строку с URL через запятую
    return ','.join(matches)


def generate_image_slides(images_html):
    """Генерация слайдов для изображений из HTML-контента"""
    slides = []
    thumbnails = []

    # Извлекаем URL из HTML
    image_urls = extract_image_urls(images_html)

    if not image_urls:
        # Если нет изображений, возвращаем заглушку
        slide = '''
                <div class="swiper-slide">
                  <div class="image-container">
                    <img src="../assets/img/no-image.jpg" alt="Нет изображения" class="main-product-image">
                  </div>
                </div>'''
        thumbnail = '''
                <div class="swiper-slide">
                  <img src="../assets/img/no-image.jpg" alt="Нет изображения" class="thumbnail-image">
                </div>'''
        return slide, thumbnail

    # Разделяем URL по запятой
    urls = [url.strip() for url in image_urls.split(',') if url.strip()]

    for i, url in enumerate(urls):
        # Используем прямые ссылки на изображения
        direct_url = url.strip()

        # Основной слайд
        slide = f'''
                <div class="swiper-slide">
                  <div class="image-container">
                    <img src="{direct_url}" 
                         alt="Изображение {i + 1}" 
                         loading="lazy"
                         class="main-product-image">
                  </div>
                </div>'''
        slides.append(slide)

        # Превью слайд
        thumbnail = f'''
                <div class="swiper-slide">
                  <img src="{direct_url}" 
                       alt="Превью {i + 1}" 
                       loading="lazy"
                       class="thumbnail-image">
                </div>'''
        thumbnails.append(thumbnail)

    return '\n'.join(slides), '\n'.join(thumbnails)


def create_css_file():
    """Создание CSS файла со стилями для страниц товаров"""
    css_content = '''/* Стили для страниц товаров */
.thumbnail-slider {
  margin-top: 15px;
  padding: 10px 0;
}

.thumbnail-slider .swiper-wrapper {
  align-items: center;
}

.thumbnail-image {
  width: 80px;
  height: 60px;
  object-fit: cover;
  border-radius: 4px;
  cursor: pointer;
  opacity: 0.6;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.thumbnail-image:hover {
  opacity: 0.8;
  transform: scale(1.05);
}

.swiper-slide-thumb-active .thumbnail-image {
  opacity: 1;
  border-color: #007bff;
}

.main-product-image {
  max-width: 100%;
  height: auto;
  max-height: 500px;
  object-fit: contain;
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  min-height: 400px;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
}

.portfolio-details-slider {
  border-radius: 8px;
  overflow: hidden;
}

.portfolio-details-slider .swiper-pagination {
  position: relative;
  margin-top: 15px;
}

.whatsapp-btn-container {
  text-align: center;
  padding: 15px 0;
}

.whatsapp-btn {
  background: #25D366;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 6px;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: background 0.3s ease;
}

.whatsapp-btn:hover {
  background: #128C7E;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Адаптивность */
@media (max-width: 768px) {
  .image-container {
    min-height: 300px;
    padding: 10px;
  }

  .main-product-image {
    max-height: 300px;
  }

  .thumbnail-image {
    width: 60px;
    height: 45px;
  }

  .thumbnail-slider .swiper-slide {
    width: auto !important;
  }
}

/* Галерея */
.portfolio-details-slider .swiper-slide {
  display: flex;
  justify-content: center;
  align-items: center;
}

.thumbnail-slider .swiper-slide {
  width: auto !important;
}
'''

    # Создаем папку assets/css если её нет
    css_dir = Path('assets/css')
    css_dir.mkdir(parents=True, exist_ok=True)

    # Сохраняем CSS файл
    css_file = css_dir / 'product-pages.css'
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

    print(f'Создан CSS файл: {css_file}')


def generate_product_pages():
    """Генерация страниц для всех товаров"""
    # Создаем CSS файл со стилями
    create_css_file()

    # Чтение данных из Excel
    df = pd.read_excel('hochushinu.xlsx')

    # Создаем папку для страниц товаров
    output_dir = Path('product_pages')
    output_dir.mkdir(exist_ok=True)

    generated_pages = []

    for index, row in df.iterrows():
        # Подготовка данных
        name = row['name']
        price = row['price']
        subcategory = row['subcategory']
        brand = row['brand']
        description = row['description']
        images_html = row['images']
        model = row['model']
        width = row['width']
        height = row['height']
        diameter = row['diameter']
        load_index = row['load_index']
        sku = row['sku']
        name_page = row['name_page']

        # Генерация контента для изображений
        image_slides, thumbnail_slides = generate_image_slides(images_html)
        category_id = get_category_id(subcategory)
        category_name = get_category_name(subcategory)

        # Заполнение шаблона
        html_content = HTML_TEMPLATE.format(
            title=name,
            description=description[:160] + '...' if len(description) > 160 else description,
            keywords=f'{brand}, {model}, шины, {subcategory}, {width}/{height}R{diameter}',
            name=name,
            category_id=category_id,
            category_name=category_name,
            image_slides=image_slides,
            thumbnail_slides=thumbnail_slides,
            brand=brand,
            model=model,
            subcategory=subcategory,
            width=width,
            height=height,
            diameter=diameter,
            load_index=load_index,
            price_formatted=format_price(price),
            sku=sku,
            full_description=description
        )

        # Сохранение файла
        filename = output_dir / name_page
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        generated_pages.append(name_page)
        print(f'Сгенерирована страница: {name_page}')

    # Создание индексного файла
    with open(output_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
    <title>Все страницы товаров</title>
</head>
<body>
    <h1>Сгенерированные страницы товаров</h1>
    <ul>''')

        for page in generated_pages:
            f.write(f'        <li><a href="{page}">{page}</a></li>\n')

        f.write('''    </ul>
</body>
</html>''')

    print(f'\nВсего сгенерировано страниц: {len(generated_pages)}')
    print(f'Файлы сохранены в папке: {output_dir}/')


if __name__ == "__main__":
    generate_product_pages()