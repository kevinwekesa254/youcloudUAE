# Software plans per segment, from "youcloud UAE Merchant Pitch" (packages p15, add-ons p16)
# and the "youcloud Self-service Data Sheet". Each text item: (english, arabic).
# Used by tools/build_pricing.py.
DH = '<span class="dh" role="img" aria-label="AED"></span>'

STD_NOTE = ('+ ' + DH + '1 per order', '+ ' + DH + '1 لكل طلب')
POW_NOTE = ('Unlimited orders', 'طلبات بلا حدود')

SEGMENTS = [
  dict(id='retail', en='Retail', ar='التجزئة', plans=[
    dict(key='std', name=('Standard', 'القياسية'), price=0, note=STD_NOTE,
      who=('For shops getting onto one system — grocery, fashion, electronics, pharmacy, perfume.', 'للمتاجر التي تنتقل إلى نظام واحد — البقالة والأزياء والإلكترونيات والصيدليات والعطور.'),
      meta=('1 user · pay per order · 500 customer records', 'مستخدم واحد · الدفع لكل طلب · 500 سجل عملاء'),
      head=('Core retail platform', 'منصة التجزئة الأساسية'),
      feats=[
        ('POS, multi-tender &amp; offline billing', 'نقاط البيع والدفع بوسائل متعددة والفوترة دون اتصال'),
        ('Stock, batches, suppliers &amp; auto-reorder', 'المخزون والدفعات والمورّدون وإعادة الطلب التلقائي'),
        ('Points, rewards &amp; birthday offers', 'النقاط والمكافآت وعروض أعياد الميلاد'),
        ('Auto-ledger, VAT reports &amp; attendance', 'قيود تلقائية وتقارير ضريبية والحضور'),
        ('Email, chat &amp; phone · 4-hr response', 'البريد والدردشة والهاتف · استجابة خلال 4 ساعات'),
      ]),
    dict(key='pow', name=('Power', 'المتقدمة'), price=99, note=POW_NOTE, popular=True,
      who=('For multi-store operators running the whole platform.', 'لمشغّلي الفروع المتعددة الذين يديرون المنصة بالكامل.'),
      meta=('1 user · unlimited orders · unlimited records', 'مستخدم واحد · طلبات بلا حدود · سجلات بلا حدود'),
      head=('Everything in Standard, plus', 'كل ما في القياسية، بالإضافة إلى'),
      feats=[
        ('youAccounts &amp; youHR included', 'youAccounts وyouHR مشمولان'),
        ('WebShop &amp; social selling included', 'المتجر الإلكتروني والبيع عبر وسائل التواصل مشمولان'),
        ('Transfers, shrinkage &amp; tiered loyalty', 'التحويل بين الفروع وإدارة الفاقد وولاء متعدد المستويات'),
        ('Dedicated success manager · QBRs', 'مدير نجاح مخصّص · مراجعات أعمال ربع سنوية'),
      ]),
    dict(key='ent', name=('Enterprise', 'المؤسسات'), price=None,
      who=('For chains, franchises and multi-brand groups.', 'للسلاسل والامتيازات التجارية والمجموعات متعددة العلامات.'),
      meta=('Unlimited stores, SKUs, staff &amp; customers', 'متاجر وأصناف وموظفون وعملاء بلا حدود'),
      head=('Everything in Power, plus', 'كل ما في المتقدمة، بالإضافة إلى'),
      feats=[
        ('Franchise &amp; policy controls', 'ضوابط الامتياز والسياسات'),
        ('SSO, API key rotation &amp; REST API', 'تسجيل دخول موحّد وتدوير مفاتيح API وREST API'),
        ('White-label storefront', 'متجر إلكتروني بعلامتك التجارية'),
        ('3PL logistics integrations', 'تكامل مع مزوّدي الخدمات اللوجستية (3PL)'),
        ('24/7 phone · 1-hr SLA', 'هاتف على مدار الساعة · استجابة خلال ساعة'),
      ]),
  ]),
  dict(id='fnb', en='F&amp;B / Restaurant', ar='المطاعم والمقاهي', plans=[
    dict(key='std', name=('Standard', 'القياسية'), price=0, note=STD_NOTE,
      who=('For cafés, salons and restaurants getting onto one system.', 'للمقاهي والصالونات والمطاعم التي تنتقل إلى نظام واحد.'),
      meta=('1 user · pay per order · 500 customer records', 'مستخدم واحد · الدفع لكل طلب · 500 سجل عملاء'),
      head=('Core restaurant platform', 'منصة المطاعم الأساسية'),
      feats=[
        ('POS, multi-tender &amp; offline billing', 'نقاط البيع والدفع بوسائل متعددة والفوترة دون اتصال'),
        ('Full KDS, 3 aggregators &amp; QR at table', 'شاشة مطبخ كاملة و3 تطبيقات توصيل وQR على الطاولة'),
        ('Ingredient stock, suppliers &amp; auto-reorder', 'مخزون المكوّنات والمورّدون وإعادة الطلب التلقائي'),
        ('Points, rewards &amp; birthday offers', 'النقاط والمكافآت وعروض أعياد الميلاد'),
        ('Auto-ledger, VAT reports &amp; attendance', 'قيود تلقائية وتقارير ضريبية والحضور'),
        ('Email, chat &amp; phone · 4-hr response', 'البريد والدردشة والهاتف · استجابة خلال 4 ساعات'),
      ]),
    dict(key='pow', name=('Power', 'المتقدمة'), price=99, note=POW_NOTE, popular=True,
      who=('For restaurant groups running every channel, HR and books.', 'لمجموعات المطاعم التي تدير كل القنوات والموارد البشرية والدفاتر.'),
      meta=('1 user · unlimited orders · unlimited records', 'مستخدم واحد · طلبات بلا حدود · سجلات بلا حدود'),
      head=('Everything in Standard, plus', 'كل ما في القياسية، بالإضافة إلى'),
      feats=[
        ('youAccounts &amp; youHR included', 'youAccounts وyouHR مشمولان'),
        ('Recipe costing &amp; all aggregators', 'تكلفة الوصفات وكل تطبيقات التوصيل'),
        ('Online &amp; social ordering included', 'الطلب الإلكتروني وعبر وسائل التواصل مشمول'),
        ('Transfers, wastage &amp; tiered loyalty', 'التحويل بين الفروع والهدر وولاء متعدد المستويات'),
        ('Dedicated success manager · QBRs', 'مدير نجاح مخصّص · مراجعات أعمال ربع سنوية'),
      ]),
    dict(key='ent', name=('Enterprise', 'المؤسسات'), price=None,
      who=('For restaurant chains, franchises and multi-brand groups.', 'لسلاسل المطاعم والامتيازات التجارية والمجموعات متعددة العلامات.'),
      meta=('Unlimited stores, SKUs, staff &amp; customers', 'متاجر وأصناف وموظفون وعملاء بلا حدود'),
      head=('Everything in Power, plus', 'كل ما في المتقدمة، بالإضافة إلى'),
      feats=[
        ('Franchise &amp; policy controls', 'ضوابط الامتياز والسياسات'),
        ('SSO, API key rotation &amp; REST API', 'تسجيل دخول موحّد وتدوير مفاتيح API وREST API'),
        ('White-label guest app', 'تطبيق ضيوف بعلامتك التجارية'),
        ('Central kitchen &amp; menu engineering', 'المطبخ المركزي وهندسة القوائم'),
        ('24/7 phone · 1-hr SLA', 'هاتف على مدار الساعة · استجابة خلال ساعة'),
      ]),
  ]),
  dict(id='self', en='Self-service', ar='الخدمة الذاتية', compact=True, plans=[
    dict(key='std', name=('Standard', 'القياسية'), price=0, note=STD_NOTE,
      who=('Kiosk and QR order-and-pay for a single outlet.', 'الكشك والطلب والدفع عبر QR لفرع واحد.'),
      meta=('1 user · ' + DH + '1 per order', 'مستخدم واحد · ' + DH + '1 لكل طلب'), head=None, feats=[]),
    dict(key='pow', name=('Power', 'المتقدمة'), price=99, note=POW_NOTE, popular=True,
      who=('For busy outlets taking the rush on kiosks, QR and self-checkout.', 'للفروع المزدحمة التي تستقبل الذروة عبر الأكشاك وQR والدفع الذاتي.'),
      meta=('1 user · unlimited orders', 'مستخدم واحد · طلبات بلا حدود'), head=None, feats=[]),
    dict(key='ent', name=('Enterprise', 'المؤسسات'), price=None,
      who=('For kiosk fleets across chains and franchises.', 'لأساطيل الأكشاك عبر السلاسل والامتيازات التجارية.'),
      meta=('Fleets, franchises, SLA', 'أساطيل · امتيازات تجارية · اتفاقية مستوى خدمة'), head=None, feats=[]),
  ],
  hardware=dict(
    tag=('Hardware · one-time', 'الجهاز · دفعة واحدة'), name='y7000', price='2,999',
    sub=('Self-service kiosk', 'كشك الخدمة الذاتية'),
    specs=[
      (('Display', 'الشاشة'), ('27" Full-HD touch', '27 بوصة Full-HD لمسية')),
      (('Payments', 'المدفوعات'), ('Chip · tap · wallets', 'شريحة · لمس · محافظ')),
      (('Printer', 'الطابعة'), ('80 mm, auto-cut', '80 مم، قصّ تلقائي')),
      (('Scanner', 'الماسح'), ('Barcode &amp; QR', 'باركود وQR')),
      (('Connectivity', 'الاتصال'), ('Wi-Fi · LAN · 4G', 'Wi-Fi · LAN · 4G')),
      (('Support', 'الدعم'), ('Next-day swap in UAE', 'استبدال في اليوم التالي داخل الإمارات')),
    ]),
  payments=dict(tag=('Payments', 'المدفوعات'), rate='2–3%', unit=('MDR', 'رسوم الخصم'),
    text=('Per card transaction · extra · card terminal required', 'لكل معاملة بطاقة · إضافية · يلزم جهاز بطاقات')),
  features=dict(tag=('Every self-service feature', 'كل ميزات الخدمة الذاتية'), items=[
    ('Self-order kiosk, QR order &amp; pay, self-checkout', 'كشك الطلب الذاتي والطلب والدفع عبر QR والدفع الذاتي'),
    ('One menu with your POS &amp; delivery apps', 'قائمة واحدة مع نقاط البيع وتطبيقات التوصيل'),
    ('Live stock — sold-out items hide', 'مخزون مباشر — تختفي الأصناف النافدة'),
    ('Modifiers, combos &amp; photo menu', 'الإضافات والوجبات المجمّعة وقائمة بالصور'),
    ('Upsell at checkout &amp; loyalty by phone or QR', 'عروض إضافية عند الدفع وولاء عبر الهاتف أو QR'),
    ('Dine-in, takeaway, pickup &amp; order-ready screen', 'داخل المطعم والسفري والاستلام وشاشة جاهزية الطلب'),
    ('Menus in EN · AR · HI · TL, allergen &amp; calorie labels', 'قوائم بالإنجليزية والعربية والهندية والتاغالوغية مع ملصقات الحساسية والسعرات'),
    ('VAT receipt — print or WhatsApp · remote menu updates', 'إيصال ضريبي مطبوع أو عبر واتساب · تحديث القائمة عن بُعد'),
  ])),
]

# Add-ons (pitch p16): (name, price html EN, price html AR)
ADDONS = [
  ('youMarketing (WABA)', DH + '33/mo + per-msg', DH + '33/شهرياً + لكل رسالة'),
  ('youInsight · AI reports', DH + '26/mo per store', DH + '26/شهرياً لكل متجر'),
  ('youLens · AI camera', DH + '62/mo + ' + DH + '26/cam', DH + '62/شهرياً + ' + DH + '26/كاميرا'),
  ('youWorkflows', DH + '44/mo', DH + '44/شهرياً'),
  ('youAccounts · full', DH + '29/mo · in Power', DH + '29/شهرياً · مشمول في المتقدمة'),
  ('youHR · full', DH + '15/staff · in Power', DH + '15/موظف · مشمول في المتقدمة'),
  ('WebShop &amp; Social', DH + '18/mo · in Power', DH + '18/شهرياً · مشمول في المتقدمة'),
  ('youLend · working capital', 'Rev-share · no monthly', 'مشاركة في الإيرادات · بلا رسوم شهرية'),
]
