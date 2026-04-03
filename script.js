// 项目数据
const projects = [
    {
        id: 1,
        title: "个人博客系统",
        description: "使用React和Node.js开发的个人博客系统，支持文章发布、评论和标签管理。",
        technologies: ["React", "Node.js", "MongoDB", "Express"],
        image: "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=modern%20blog%20website%20design&image_size=landscape_4_3"
    },
    {
        id: 2,
        title: "电商网站",
        description: "基于Vue.js的电商网站，包含商品展示、购物车和支付功能。",
        technologies: ["Vue.js", "Vuex", "Element UI", "Axios"],
        image: "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=e-commerce%20website%20design&image_size=landscape_4_3"
    },
    {
        id: 3,
        title: "数据可视化仪表盘",
        description: "使用D3.js开发的数据可视化仪表盘，展示销售数据和用户行为分析。",
        technologies: ["D3.js", "JavaScript", "HTML5", "CSS3"],
        image: "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=data%20visualization%20dashboard&image_size=landscape_4_3"
    },
    {
        id: 4,
        title: "移动应用原型",
        description: "使用React Native开发的移动应用原型，实现了用户认证和数据展示功能。",
        technologies: ["React Native", "Redux", "Firebase"],
        image: "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=mobile%20app%20prototype%20design&image_size=landscape_4_3"
    }
];

// 生成项目卡片
function generateProjectCards() {
    const projectsGrid = document.querySelector('.projects-grid');
    if (!projectsGrid) return;

    projects.forEach(project => {
        const projectCard = document.createElement('div');
        projectCard.className = 'project-card';
        projectCard.innerHTML = `
            <div class="project-image">
                <img src="${project.image}" alt="${project.title}">
            </div>
            <div class="project-content">
                <h3>${project.title}</h3>
                <p>${project.description}</p>
                <div class="project-tech">
                    ${project.technologies.map(tech => `<span class="tech-tag">${tech}</span>`).join('')}
                </div>
            </div>
        `;
        projectsGrid.appendChild(projectCard);
    });
}

// 滚动动画
function handleScrollAnimation() {
    const elements = document.querySelectorAll('.about, .projects, .contact');
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.classList.add('fade-in');
        }
    });
}

// 导航栏滚动效果
function handleNavbarScroll() {
    const header = document.querySelector('header');
    if (!header) return;
    
    if (window.scrollY > 100) {
        header.style.backgroundColor = 'rgba(51, 51, 51, 0.9)';
    } else {
        header.style.backgroundColor = '#333';
    }
}

// 平滑滚动到锚点
function handleSmoothScroll() {
    const links = document.querySelectorAll('nav a');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// 页面加载完成后执行
window.addEventListener('DOMContentLoaded', function() {
    generateProjectCards();
    handleSmoothScroll();
    handleScrollAnimation();
    handleNavbarScroll();
});

// 滚动时执行
window.addEventListener('scroll', function() {
    handleScrollAnimation();
    handleNavbarScroll();
});