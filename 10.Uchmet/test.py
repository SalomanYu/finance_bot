import re

text = """    <div class="row">
        <div class="col-lg-3 col-md-3 col-sm-4 col-xs-12 video-thumbnail vert-offset">
            <div class="video-thumbnail__body"
                onclick="showPopupYoutubeVideo('//www.youtube.com/embed/2Yn-5Hx7NEQ?autoplay=1&amp;rel=0&amp;end=0', 'Видео презентация', 'https://www.uchmet.ru/'); return false">
                <img alt="Платные образовательные услуги в условиях реализации ФЗ «Об образовании в РФ» - видеопрезентация"
                    class="video-thumbnail__preview"
                    src="/upload/iblock/5d1/5d136957a2b5bfab34472d221a46e0b9/maxresdefault.jpg"
                    title="Платные образовательные услуги в условиях реализации ФЗ «Об образовании в РФ» - видеопрезентация" />
            </div>
        </div>
    </div>
    <div class="special-offer">
        <div class="special-offer__inner">
            <h3 class="special-offer__title">Спецпредложение</h3>
            <div class="special-offer__text">
                <p> Пополнив свой личный счёт в интернет-магазине <a href="https://www.uchmag.ru/"
                        target="_blank">«УчМаг»</a> на сумму 400 рублей, Вы сможете <strong>бесплатно</strong> получить
                    доступ к материалам данного офлайн-мероприятия и <strong>бесплатно</strong> получить сертификат.
                </p>
                <p> Денежные средства на Ваш <a href="https://www.uchmag.ru/personal/accaunt/" target="_blank">личный
                        счёт</a> <strong>зачисляются в полном размере</strong>, и ими можно будет воспользоваться в
                    любое удобное Вам время при покупке любых товаров в интернет-магазине <a
                        href="https://www.uchmag.ru/" target="_blank">«УчМаг»</a> (за исключением купонов на пополнение
                    личного счёта). </p>
            </div>
            <div class="special-offer__button"> <a class="btn btn-default btn-md" data-simple-auth-reg="true"
                    href="/order/add.php?pid=382262&amp;q=1&amp;eid=383483" onclick="
                                        if(typeof ym != 'undefined') {
                                                ym('25806965', 'reachGoal', 'EventSpecialOfferClick');
                                        }"><i class="fa fa-bell-o mrx"></i>Принять спецпредложение</a> </div>
        </div>
    </div>
    <p>Приглашаем руководителей ОО и ДОО, заместителей руководителя по УМР, методистов, старших воспитателей,
        руководителей методических объединений принять участие в <strong>offline-вебинаре «Платные образовательные
            услуги в условиях реализации ФЗ «Об образовании в РФ». </strong></p>
    <p>Формат offline-вебинара предполагает, что вы можете пользоваться материалами (выступление, презентация)
        круглосуточно в любое удобное вам время, а также связаться с автором и получить ответы на интересующие вас
        вопросы.</p>
    <p>Вашему вниманию предложены для рассмотрения следующие<b> вопросы:</b>
    </p>
    <ol>
        <li> Нормативно-правовая база Федерального уровня.
            <ul style="list-style-type: none;">
                <li>1.1. Закон о защите прав потребителей.</li>
                <li>1.2. Статьи Гражданского кодекса РФ.</li>
                <li>1.3. Статьи Федерального закона «Об образовании в Российской Федерации».</li>
                <li>1.4. Постановление Правительства РФ «Об утверждении правил оказания платных образовательных услуг».
                </li>
                <li>1.5. Проект приказа Минобрнауки РФ «Об утверждении примерной формы договора об образовании при
                    приеме на обучение».</li>
            </ul>
        </li>
        <li> Нормативная база ОУ.</li>
    </ol>
    <ul style="list-style-type: none;">
        <li>2.1. Положение о платных образовательных услугах.</li>
        <li>2.2. Положение о порядке привлечения внебюджетных средств.</li>
        <li>2.3. Договор о предоставлении ПОУ.</li>
        <li>2.4. Должностные инструкции.</li>
        <li>2.5. Протокол собрания управляющего совета. </li>
        <li>2.6. Выписка из Устава ОУ.</li>
        <li>2.7. Приказы ОУ «Об организации работы по оказанию платных образовательных услуг».</li>
    </ul>
    <li> Информация для сайта ОУ и стенда «Уголок потребителя».</li>
    <ul style="list-style-type: none;">
        <li>3.1. Заявление родителей.</li>
        <li>3.2. Перечень ПОУ.</li>
        <li>3.3. Прейскурант тарифов и цен ПОУ.</li>
        <li>3.4. Объемы ПОУ.</li>
        <li>3.5. Расписание занятий.</li>
        <li>3.6. Порядок приема и требования к поступающим для изучения образовательных программ на платной основе.</li>
        <li>3.7. Квитанция по оплате.</li>
    </ul>
    <li> Порядок прекращения оказания платных образовательных услуг.</li>
    <ul style="list-style-type: none;">
        <li>4.1. Порядок прекращения оказания платных образовательных услуг.</li>
        <li>4.2. Уведомление о расторжении договора об оказании ПОУ.</li>
        <li>4.3. СОГЛАШЕНИЕ о расторжении договора об оказании платных образовательных услуг.</li>
    </ul>
    <li> Программы платных образовательных услуг.</li>
    <li> Отчеты, аналитические справки.</li>
    <p><b>Ведущий вебинара: </b><br /><b><i>Лободина Наталья Викторовна</i></b>, учитель начальных классов МОУ СШ № 103
        г. Волгограда, Почетный работник общего образования Российской Федерации.</p>
    <p><b>Теги:</b> <a
            href="https://www.uchmag.ru/search/?q=%D0%A4%D0%93%D0%9E%D0%A1&amp;s=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA"
            target="_blank">ФГОС</a>, <a
            href="https://www.uchmag.ru/search/?q=%D0%A4%D0%97&amp;s=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8"
            target="_blank">ФЗ</a>, <a
            href="https://www.uchmag.ru/search/?q=%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F&amp;s=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA"
            target="_blank">образовательная организация</a>, <a href="https://www.uchmag.ru/estore/e240964/"
            target="_blank">платные образовательные услуги</a>, <a
            href="https://www.uchmag.ru/search/?q=%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE-%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B1%D0%B0%D0%B7%D0%B0&amp;s=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8"
            target="_blank">нормативно-правовая база</a>, <a
            href="https://www.uchmag.ru/search/?q=%D0%B2%D0%BD%D0%B5%D0%B1%D1%8E%D0%B4%D0%B6%D0%B5%D1%82%D0%BD%D1%8B%D0%B5+%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0&amp;s=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA"
            target="_blank">внебюджетные средства</a>. </p>
    <h3>Сообщество</h3>
    <script src="https://vk.com/js/api/openapi.js?168" type="text/javascript"></script>
    <!-- VK Widget -->
    <div class="mtm" id="vk_groups"></div>
    <script type="text/javascript">
        VK.Widgets.Group('vk_groups', {
            width: 245,
            height: 200,
            mode: 3,
            no_cover: 0,
            wide: 0,
            $color1: 'FFFFFF',
            $color2: '000000',
            $color3: '4D6090',
        }, 137813509);
    </script>
    </div>
"""

print(re.findall("<script.*?\>(.*?)</script>", text))