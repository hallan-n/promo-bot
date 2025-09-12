from playwright.async_api import Browser, Page


async def get_stealth_page(browser: Browser, mobile: bool = False) -> Page:
    if mobile:
        config = {
            "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1",
            "viewport": {"width": 375, "height": 667},
            "device_scale_factor": 2,
            "is_mobile": True,
            "has_touch": True,
            "locale": "pt-BR",
            "timezone_id": "America/Sao_Paulo",
            "ignore_https_errors": True
        }
    else:
        config = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "viewport": None,
            "device_scale_factor": 1,
            "is_mobile": False,
            "has_touch": False,
            "locale": "pt-BR",
            "timezone_id": "America/Sao_Paulo",
            "ignore_https_errors": True
        }

    context = await browser.new_context(**config)
    page = await context.new_page()

    await page.add_init_script(
        """
    // Remover navigator.webdriver
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });

    // Adicionar plugins falsos
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5],
    });

    // Adicionar idiomas
    Object.defineProperty(navigator, 'languages', {
        get: () => ['pt-BR', 'pt'],
    });

    // Simular chrome runtime
    window.chrome = {
        runtime: {},
        loadTimes: () => {},
        csi: () => {},
    };

    // WebGL Vendor spoofing
    const getParameter = WebGLRenderingContext.prototype.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        if (parameter === 37445) return 'Intel Inc.';
        if (parameter === 37446) return 'Intel Iris OpenGL Engine';
        return getParameter(parameter);
    };
    """
    )
    return page
